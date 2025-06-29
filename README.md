# Excel Comparator

🧮 A Python tool that compares two Excel files (`old` and `new`) and detects:
- ✅ Added rows
- 🗑️ Removed rows
- ✏️ Changed rows (based on ID)
  
### 📦 Features
- Compares by unique `ID`
- Shows changed rows side-by-side
- Saves result into `compare_v2.xlsx` with 3 sheets: `Added`, `Removed`, `Changed`

---

## 🚀 How to Use

1. Place your Excel files in the project folder:
   - `employees_old.xlsx`
   - `employees_new.xlsx`

2. Run the script:

```bash
python compare.py
