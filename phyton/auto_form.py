import tkinter as tk
from tkinter import messagebox
import sqlite3

DB_FILE = 'autoverhuur.sql'

def get_auto_by_id(auto_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM Auto WHERE AutoID=?', (auto_id,))
    row = c.fetchone()
    conn.close()
    return row

def save_auto(data, auto_id=None):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    if auto_id:
        c.execute('''UPDATE Auto SET AutoMerkID=?, AutoBrandstofID=?, AutoType=?, AutoVerbruik=?, AutoTankCapaciteit=?, AutoTankInhoud=?, AutoActief=? WHERE AutoID=?''',
                  (*data, auto_id))
    else:
        c.execute('''INSERT INTO Auto (AutoMerkID, AutoBrandstofID, AutoType, AutoVerbruik, AutoTankCapaciteit, AutoTankInhoud, AutoActief) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                  data)
    conn.commit()
    conn.close()

def form_window(auto_id=None):
    def get_merken():
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('SELECT MerkID, MerkNaam FROM Merk WHERE MerkActief=1 ORDER BY MerkNaam ASC')
        merken = c.fetchall()
        conn.close()
        return merken

    def get_brandstoffen():
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('SELECT BrandstofID, BrandstofOmschrijving FROM Brandstof WHERE BrandstofActief=1 ORDER BY BrandstofOmschrijving ASC')
        brandstoffen = c.fetchall()
        conn.close()
        return brandstoffen

    def load_data():
        if auto_id:
            row = get_auto_by_id(auto_id)
            if row:
                # Set dropdown for Merk by name
                merk_id = row[1]
                for idx, (mid, mname) in enumerate(merken):
                    if mid == merk_id:
                        var_merk_name.set(mname)
                        break
                # Set dropdown for Brandstof by name
                brandstof_id = row[2]
                for idx, (bid, bname) in enumerate(brandstoffen):
                    if bid == brandstof_id:
                        var_brandstof_name.set(bname)
                        break
                # Set other fields
                for i, val in enumerate(row[3:7]):
                    entries[i].delete(0, tk.END)
                    entries[i].insert(0, str(val))
                var_actief.set(bool(row[7]))

    def on_save():
        try:
            # Get selected MerkID from dropdown by name
            selected_merk_name = var_merk_name.get()
            merk_id = None
            for mid, mname in merken:
                if mname == selected_merk_name:
                    merk_id = mid
                    break
            if not selected_merk_name or merk_id is None:
                raise Exception('Selecteer een merk!')
            # Get selected BrandstofID from dropdown by name
            selected_brandstof_name = var_brandstof_name.get()
            brandstof_id = None
            for bid, bname in brandstoffen:
                if bname == selected_brandstof_name:
                    brandstof_id = bid
                    break
            if not selected_brandstof_name or brandstof_id is None:
                raise Exception('Selecteer een brandstof!')
            # Get other fields
            data = [
                int(merk_id),
                int(brandstof_id),
                entries[0].get(),
                int(entries[1].get()),
                int(entries[2].get()),
                int(entries[3].get()),
                bool(var_actief.get())
            ]
            save_auto(data, auto_id)
            messagebox.showinfo('Success', 'Auto saved!')
            root.destroy()
        except Exception as ex:
            messagebox.showerror('Error', str(ex))

    root = tk.Tk()
    root.title('Auto Form')
    labels = ['AutoMerkID', 'AutoBrandstofID', 'AutoType', 'AutoVerbruik', 'AutoTankCapaciteit', 'AutoTankInhoud', 'AutoActief']
    # Get merken for dropdown
    merken = get_merken()
    merk_names = [m[1] for m in merken]
    merk_names.insert(0, '')
    var_merk_name = tk.StringVar(value='')
    tk.Label(root, text=labels[0]).grid(row=0, column=0)
    merk_menu = tk.OptionMenu(root, var_merk_name, *merk_names)
    merk_menu.grid(row=0, column=1)

    # Get brandstoffen for dropdown
    brandstoffen = get_brandstoffen()
    brandstof_names = [b[1] for b in brandstoffen]
    brandstof_names.insert(0, '')
    var_brandstof_name = tk.StringVar(value='')
    tk.Label(root, text=labels[1]).grid(row=1, column=0)
    brandstof_menu = tk.OptionMenu(root, var_brandstof_name, *brandstof_names)
    brandstof_menu.grid(row=1, column=1)

    entries = []
    # AutoType
    tk.Label(root, text=labels[2]).grid(row=2, column=0)
    entry_type = tk.Entry(root)
    entry_type.grid(row=2, column=1)
    entries.append(entry_type)
    # AutoVerbruik (default 5)
    tk.Label(root, text=labels[3]).grid(row=3, column=0)
    entry_verbruik = tk.Entry(root)
    entry_verbruik.insert(0, '5')
    entry_verbruik.grid(row=3, column=1)
    entries.append(entry_verbruik)
    # AutoTankCapaciteit (default 50)
    tk.Label(root, text=labels[4]).grid(row=4, column=0)
    entry_tankcap = tk.Entry(root)
    entry_tankcap.insert(0, '50')
    entry_tankcap.grid(row=4, column=1)
    entries.append(entry_tankcap)
    # AutoTankInhoud (default 15)
    tk.Label(root, text=labels[5]).grid(row=5, column=0)
    entry_tankinh = tk.Entry(root)
    entry_tankinh.insert(0, '15')
    entry_tankinh.grid(row=5, column=1)
    entries.append(entry_tankinh)
    var_actief = tk.BooleanVar(value=True)
    tk.Label(root, text=labels[-1]).grid(row=6, column=0)
    cb = tk.Checkbutton(root, variable=var_actief, onvalue=True, offvalue=False)
    cb.grid(row=6, column=1)
    tk.Button(root, text='Save', command=on_save).grid(row=7, column=0, columnspan=2)
    load_data()
    root.mainloop()

if __name__ == '__main__':
    # To create a new Auto, call form_window()
    # To edit an existing Auto, call form_window(auto_id)
    form_window()
