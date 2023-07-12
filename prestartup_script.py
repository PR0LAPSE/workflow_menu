import os
import shutil
import requests
from bs4 import BeautifulSoup
import folder_paths

# gdrive_workflow = 'C:\\ui\\test' # для windows
gdrive_workflow = '/content/drive/MyDrive/SD/ComfyUI/workflow' # для Colab
colab_workflow = os.path.join(os.path.dirname(folder_paths.__file__), "web", "workflow")
custom_nodes_path = os.path.join(os.path.dirname(folder_paths.__file__), "custom_nodes")
wcrepo = "PR0LAPSE/wc"

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

response = requests.get(f"https://github.com/{wcrepo}")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    json_files = []
    py_files = []
    elements = soup.find_all("a", {"data-turbo-frame": "repo-content-turbo-frame"})
    for element in elements:
        text = element.text
        if text.endswith(".json"):
            json_files.append(text)
        elif text.endswith(".py"):
            py_files.append(text)

    os.makedirs(colab_workflow, exist_ok=True)
    for json_file in json_files:
        url = f"https://raw.githubusercontent.com/{wcrepo}/main/{json_file.replace(' ', '%20')}"
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(colab_workflow, json_file), "wb") as f:
                f.write(response.content)
                print(f"{json_file} успешно скачан")
        else:
            print(f"ошибка при загрузке  {json_file}:", response.status_code)

    os.makedirs(custom_nodes_path, exist_ok=True)
    for py_file in py_files:
        url = f"https://raw.githubusercontent.com/{wcrepo}/main/{py_file.replace(' ', '%20')}"
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(custom_nodes_path, py_file), "wb") as f:
                f.write(response.content)
                print(f"{py_file} успешно скачан")
        else:
            print(f"ошибка при загрузке {py_file}:", response.status_code)
else:
    print("страницу с репой воркфлоу загрузить не получилось:", response.status_code)
