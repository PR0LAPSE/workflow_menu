import os
import shutil
import folder_paths

comfy_path = os.path.dirname(folder_paths.__file__)
workflow_menu_path = os.path.dirname(__file__)
custom_nodes_path = os.path.join(comfy_path, 'custom_nodes')
js_path = os.path.join(comfy_path, "web", "extensions")
js_src_path = os.path.join(workflow_menu_path, "js", "select_wotkflow.js")
js_dest_path = os.path.join(js_path, "workflow_menu")

if not os.path.exists(js_dest_path):
    os.makedirs(js_dest_path)
if os.path.exists(js_dest_path) and len(os.listdir(js_dest_path)) > 0:
    files = [os.path.join(js_dest_path, f) for f in os.listdir(js_dest_path)]
    for file in files:
        try:
            os.remove(file)
        except Exception as e:
            print(f"{e}")
shutil.copy(js_src_path, js_dest_path)

colab_workflow = os.path.join(os.path.dirname(folder_paths.__file__), "web", "workflow")
workflows_list = os.path.join(os.path.dirname(folder_paths.__file__), "web", "extensions", "workflow_menu", "workflows_paths.txt")
if os.path.exists(workflows_list):
    os.remove(workflows_list)
file_names = []
for file in os.listdir(colab_workflow):
    if file.endswith(".json"):
        file_names.append(file)

with open(workflows_list, "w") as f:
    for name in file_names:
        f.write("workflow/" + name + "\n")
    f.seek(0, os.SEEK_END)
    f.seek(f.tell() - 1, os.SEEK_SET)
    f.truncate()

NODE_CLASS_MAPPINGS = {}
__all__ = ['NODE_CLASS_MAPPINGS'] 