import os

from archive_context_manager import ArchiveContextManager

files_directory_path = 'files_dir'

with ArchiveContextManager('archive') as archive_manager:
    for file_name in os.listdir(files_directory_path):
        archive_manager.write(os.path.join(files_directory_path, file_name))
