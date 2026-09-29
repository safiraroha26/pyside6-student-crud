import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem
)

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

import database


class Aplikasi(QWidget):
    def __init__(self):
        super().__init__()

        database.buat_table()

        import os
        import sys

        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS  # folder sementara saat exe jalan
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)

        ui_path = resource_path("ui/form.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(file)
        file.close()

        self.id_terpilih = None

        self.input_nama = self.window.findChild(QLineEdit, "input_nama")
        self.input_kelas = self.window.findChild(QLineEdit, "input_kelas")
        self.btn_simpan = self.window.findChild(QPushButton, "btn_simpan")
        self.btn_update = self.window.findChild(QPushButton, "btn_update")
        self.btn_hapus = self.window.findChild(QPushButton, "btn_hapus")
        self.table = self.window.findChild(QTableWidget, "table_siswa")

        self.btn_simpan.clicked.connect(self.simpan_data)
        self.btn_update.clicked.connect(self.update_data)
        self.btn_hapus.clicked.connect(self.hapus_data)
        self.table.cellClicked.connect(self.pilih_data)
        
        self.tampilkan_data() 
        self.window.show()
    
    def pilih_data(self, row, column):
        self.id_terpilih = self.table.item(row, 0).text()
        self.input_nama.setText(self.table.item(row, 1).text())
        self.input_kelas.setText(self.table.item(row, 2).text())

    def update_data(self):
        if self.id_terpilih:
            nama = self.input_nama.text()
            kelas = self.input_kelas.text()

        database.update_siswa(self.id_terpilih, nama, kelas)
        self.tampilkan_data()

    def hapus_data(self):
        if self.id_terpilih:
            database.hapus_siswa(self.id_terpilih)
            self.tampilkan_data()

    def tampilkan_data(self):
        data = database.ambil_siswa()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(3)


        for row_index, row_data in enumerate(data):
            for col_index, item in enumerate(row_data):
                self.table.setItem(
                    row_index,
                    col_index,
                    QTableWidgetItem(str(item))
                )

    def simpan_data(self):
        nama = self.input_nama.text()
        kelas = self.input_kelas.text()
        database.insert_siswa(nama, kelas)
        print("Data berhasil disimpan")
        self.tampilkan_data()
        print(database.tampil_siswa())


if __name__ =="__main__" :
    app = QApplication(sys.argv)
    aplikasi = Aplikasi()
    sys.exit(app.exec())

