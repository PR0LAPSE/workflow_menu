import os
import shutil
import folder_paths

# gdrive_workflow = 'C:\\ui\\test' # для windows
gdrive_workflow = '/content/drive/MyDrive/SD/ComfyUI/workflow' # для Colab
colab_workflow = os.path.join(os.path.dirname(folder_paths.__file__), "web", "workflow")

if not os.path.exists(gdrive_workflow):
    os.makedirs(gdrive_workflow)
    print("на гуглодиске создана папка SD/ComfyUI/workflow - там надо хранить свои воркфлоу!")
if not os.path.exists(colab_workflow):
    os.makedirs(colab_workflow)
if os.path.exists(gdrive_workflow) and len(os.listdir(gdrive_workflow)) > 0:
  files = [f for f in os.listdir(gdrive_workflow) if f.endswith('.json')]
  for file in files:
      src = os.path.join(gdrive_workflow, file)
      dst = os.path.join(colab_workflow, file)
      try:
          os.symlink(src, dst)
      except Exception as e:
          print(f"не удалось создать симлинк '{file}': {e}")
      else:
          print(f"симлинк '{file}' успешно создан")
    
