import os, shutil

class FileOrganiser:

    def __init__(self, path):
        self.path = path

    def get_extensions(self):
        ext_list = []
        for f in os.listdir(self.path):
            file_ext = (f[-4:].lstrip('.'))
            if file_ext not in ext_list:
                ext_list.append(file_ext)
        return ext_list
    
    def create_dirs(self, ext_list):
        dir_names = []
        for e in ext_list:
            folder = e + ' ' + 'folder'
            dir_names.append(folder)
        dir_paths = [os.path.join(self.path, folder) for folder in dir_names]
        for d in dir_paths:
            if not os.path.exists(d):
                os.makedirs(d)
        return dir_paths
    
    def sort_files(self):
        ext_list = self.get_extensions()
        dir_paths = self.create_dirs(ext_list)
        for file in os.listdir(self.path):
            ext = file[-4:].lstrip('.')
            destination = ext + ' folder'
            cur_path = os.path.join(self.path, file)
            dest_path = os.path.join(self.path, destination, file)
            if os.path.isfile(cur_path) and not os.path.exists(dest_path):
                shutil.move(cur_path, dest_path)

path = r"C:\Users\Razer\Documents\Data Analyst Lessons\Python Tutorials\File Sorter"
organise = FileOrganiser(path)
organise.sort_files()