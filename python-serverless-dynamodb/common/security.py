import os
import function_shield

function_shield.configure({
    "policy": {
        "outbound_connectivity": "allow",
        "read_write_tmp": "block",
        "create_child_process": "block",
        "read_handler": "block"
    },
    "token": os.environ['FUNCTION_SHIELD_TOKEN']
})
