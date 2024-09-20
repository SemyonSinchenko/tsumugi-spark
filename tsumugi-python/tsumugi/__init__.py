import sys
from pathlib import Path

proto_root = Path(__file__).parent.joinpath("proto")
if str(proto_root.absolute()) not in sys.path:
    sys.path.append(str(proto_root.absolute()))
