from backup_context_manager import BackupContextManager

with BackupContextManager('important_file.txt') as important_file:
    with open(important_file, 'w') as file:
        for number in range(5):
            file.write(f"Added line {number} \n")
