#verify_installation

import sys 
import importlib
packages = ["numpy","pandas","sklearn","skfuzzy","cv2","matplotlib","nltk"]
for pkg in packages:
    try:
        m = importlib.import_module(pkg)
        print(f"(pkg): OK, version = {getattr(m, '__version__', 'unknown')}")
    except Exception as e:
        print(f"(pkg):ERROR -> (e)")

print("Python:", sys.version)