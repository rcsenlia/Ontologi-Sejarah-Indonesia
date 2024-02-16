# Weekly Notes

## Januari 2024
- ### Rabu, 31 Januari 2024
    #### Recap:
    Pada pekan ini, saya mencoba mempelajari beberapa ontologi yang sudah ada untuk peristiwa atau *event* seperti CIDOC CRM dan WarSampo. Saya juga mencari sumber data yang mungkin dapat digunakan seperti DBPedia dan Wikipedia. Untuk mengambil data dari DBPedia, saya mempelajari ulang projek akhir mata kuliah Jejaring Semantik dan telah berhasil melakukan query terhadap SPARQL *endpoint* DBPedia menggunakan *library* `SPARQLWrapper`. Pada DBPedia, saya menemukan kendala seperti tanggal yang tidak sesuai seperti pada [Kerusuhan Mei 1998](https://dbpedia.org/page/May_1998_riots_of_Indonesia) serta penggunaan properti yang berbeda untuk hal yang sama seperti tanggal (dbo:date dan dbp:date). Untuk mendapatkan seluruh data peristiwa pada masa Orde Baru, dapat digunakan [Kategori: Orde Baru](https://dbpedia.org/page/Category:New_Order_(Indonesia)). Untuk data dari Wikipedia, perlu dilakukan scrapping pada halaman [Kategori: Orde Baru](https://id.wikipedia.org/wiki/Kategori:Orde_Baru) untuk mendapatkan seluruh halaman peristiwa Orde Baru.

    #### Notes Bimbingan:
    Dapat mengeksplor lebih lanjut data dari Wikipedia, khususnya menggunakan file *dumps* [idwiki](https://dumps.wikimedia.org/idwiki/). Selanjutnya, mencoba mencari halaman yang memiliki kategori sejarah Indonesia dan memisahkan halaman yang memiliki *infobox* dan yang tidak. Untuk halaman yang tidak memiliki *infobox* perlu dilakukan penulusuran lebih dalam.


## Februari 2024
- ### Rabu, 7 Februari 2024
    #### Recap:
    Pada pekan ini, saya mencoba mengeksplor data pada idwiki. Dengan menggunakan berbagai referensi, seperti *repository* [`wikipedia-data-science`](https://github.com/WillKoehrsen/wikipedia-data-science/blob/master/notebooks/Downloading%20and%20Parsing%20Wikipedia%20Articles.ipynb) dan Tugas Pemrograman mata kuliah Perolehan Informasi, saya berhasil melakukan *indexing* terhadap seluruh halaman berdasarkan kategori. Kendala yang saya temukan adalah terdapat konsep subkategori dan untuk setiap halaman tidak dijamin memiliki seluruh superkategori dari kategori yang dimiliki. Solusi untuk saat ini adalah mengumpulkan seluruh kategori yang mungkin berhubungan dengan data sejarah Indonesia secara manual. Selain itu, saya juga telah berhasil memisahkan halaman yang memiliki *infobox* dan tidak dengan memanfaatkan *template* yang ada pada halaman tersebut.

    #### Notes Bimbingan:
    Untuk beberapa halaman, seperti untuk masa kolonialisme, dapat digunakan *template* yang memiliki informasi lebih lengkap dibandingkan menggunakan kategori. Selain itu, untuk data-data dari *infobox* yang berupa `json` perlu diproses lebih lanjut karena beberapa penamaan *key* yang kurang memiliki makna. Selanjutnya, dapat mengeksplorasi file *dumps* enwiki dan mencari referensi ontologi lain yang dapat digunakan.

