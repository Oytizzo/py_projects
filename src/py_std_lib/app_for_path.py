from pathlib import Path
from time import ctime
import shutil

source = Path(r"py_std_lib\app_for_path.py")
target = Path() / "__init__.py"

shutil.copy(source, target)

# print(Path.home())
# path = Path(r"py_std_lib\app_for_path.py")
# path.exists()
# path.rename("app.txt")
# path.unlink()
# print(ctime(path.stat().st_ctime))

# path.read_bytes()
# path.read_text()
# path.write_text("....")
# path.write_bytes()
