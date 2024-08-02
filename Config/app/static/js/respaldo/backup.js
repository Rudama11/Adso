
        document.getElementById('select-file-button').addEventListener('click', function() {
            document.getElementById('backup-file-input').click();
        });

        document.getElementById('backup-file-input').addEventListener('change', function() {
            var fileName = this.files[0].name;
            document.getElementById('file-name').textContent = fileName;
        });