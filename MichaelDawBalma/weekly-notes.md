# Weekly Notes

---
## Februari 2024
- ### Rabu, 7 Februari 2024
    #### Recap:
    Pekan ini saya mencoba untuk eksplor data mengenai id-wiki dumps. Hasil akhir yang didapatkan,
    saya dapat me-retrieve seluruh artikel yang memiliki Kategori: Sejarah Indonesia. Setelah seluruh artikel
    yang sesuai didapatkan, saya dapat memisahkan artikel yang memiliki infobox dengan yang tidak.\
    Permasalahan yang muncul adalah ternyata tidak seluruh artikel yang berkaitan dengan Sejarah Indonesia
    memiliki Kategori: Sejarah Indonesia. Oleh karena itu, harus dilakukan extract; cari kategori secara manual,
    sehingga dapat diambil datanya.
    #### Notes Bimbingan:
    - Simbol {{x}} pada xml data wikipedia menandakan x adalah template. Infobox termasuk kedalam template.
    (Lihat wikipedia:list of infoboxes dan wikipedia:templates help).
    - Infobox part of template! artinya infobox military punya template misal masa pengabdian, 
    dari negara mana, pangkat, etc.
    - Menurut richie, better berangkat dari infobox (ex military infobox) daripada kategori:sejarah indonesia, 
    soalnya ga semua ada di sejarah indonesia (ex:pattimura) serta Hasil json harus dimapping lagi; tidak bisa
    langsung dipakai.
    #### Todo:
    - [ ] Cari kategori yang sesuai, di list di spreadsheet, dioper ke temen-temen yang lain
    - [ ] Cari vocabulary yang cocok, baca referensi; ex: War Sampo
    - [x] Buat readme.md tentang catatan mingguan
    - [ ] Mengisi bimbingan pada Siak-NG
    #### Goals:
    - [ ] Menyelesaikan dataset wikipedia
    - [ ] Mencari artikel dari en.wiki
    - [ ] Solve britannica (sementara fokus dulu ke wiki)
