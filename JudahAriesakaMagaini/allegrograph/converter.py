data = [
        {
            "nama_peristiwa": "Kedatangan Bangsa Eropa",
            "tahun_peristiwa": 1602,
            "latitude": -6.175110,
            "longitude": 106.865036
        },
        {
            "nama_peristiwa": "Lahirnya Budi Utomo",
            "tahun_peristiwa": 1908,
            "latitude": -6.186486,
            "longitude": 106.834091
        },
        {
            "nama_peristiwa": "Sumpah Pemuda",
            "tahun_peristiwa": 1928,
            "latitude": -6.199986,
            "longitude": 106.832260
        },
        {
            "nama_peristiwa": "Indonesia Dikuasai Jepang",
            "tahun_peristiwa": 1942,
            "latitude": -6.175110,
            "longitude": 106.865036
        },
        {
            "nama_peristiwa": "Proklamasi Kemerdekaan Indonesia",
            "tahun_peristiwa": 1945,
            "latitude": -6.199986,
            "longitude": 106.832260
        },
        {
            "nama_peristiwa": "Pertempuran Medan Area",
            "tahun_peristiwa": 1945,
            "latitude": 3.595196,
            "longitude": 98.672223
        },
        {
            "nama_peristiwa": "Pertempuran Surabaya",
            "tahun_peristiwa": 1945,
            "latitude": -7.257472,
            "longitude": 112.752088
        },
        {
            "nama_peristiwa": "Perjanjian Linggarjati",
            "tahun_peristiwa": 1946,
            "latitude": -6.819562,
            "longitude": 108.291649
        },
        {
            "nama_peristiwa": "Pemberontakan DI/TII",
            "tahun_peristiwa": 1948,
            "latitude": -7.801194,
            "longitude": 110.364917
        },
        {
            "nama_peristiwa": "Serangan Umum 1 Maret",
            "tahun_peristiwa": 1949,
            "latitude": -7.801194,
            "longitude": 110.364917
        },
        {
            "nama_peristiwa": "Konferensi Meja Bundar",
            "tahun_peristiwa": 1949,
            "latitude": 52.370216,
            "longitude": 4.895168
        },
        {
            "nama_peristiwa": "Dekrit Presiden 5 Juli",
            "tahun_peristiwa": 1959,
            "latitude": -6.175110,
            "longitude": 106.865036
        },
        {
            "nama_peristiwa": "Peristiwa G30S/PKI",
            "tahun_peristiwa": 1965,
            "latitude": -6.175110,
            "longitude": 106.865036
        },
        {
            "nama_peristiwa": "Supersemar",
            "tahun_peristiwa": 1966,
            "latitude": -6.175110,
            "longitude": 106.865036
        },
        {
            "nama_peristiwa": "Pembantaian Warga Tionghoa di Batavia",
            "tahun_peristiwa": 1740,
            "latitude": -6.175110,
            "longitude": 106.865036
        },
        {
            "nama_peristiwa": "Perang Padri",
            "tahun_peristiwa": 1803,
            "latitude": -0.305556,
            "longitude": 100.369167
        },
        {
            "nama_peristiwa": "Peristiwa Rengasdengklok",
            "tahun_peristiwa": 1945,
            "latitude": -6.148056,
            "longitude": 107.293056
        },
        {
            "nama_peristiwa": "Perjanjian Renville",
            "tahun_peristiwa": 1948,
            "latitude": -6.175110,
            "longitude": 106.865036
        },
        {
            "nama_peristiwa": "Perundingan Roem Royen",
            "tahun_peristiwa": 1949,
            "latitude": -6.175110,
            "longitude": 106.865036
        },
        {
            "nama_peristiwa": "Pertempuran Bandung Lautan Api",
            "tahun_peristiwa": 1946,
            "latitude": -6.917464,
            "longitude": 107.619123
        }
    ]

ttl_data = "@prefix ex: <http://example.com/> .\n\n"

for item in data:
    event_name = item["nama_peristiwa"].replace(" ", "")
    ttl_data += f'ex:{event_name}\n'
    ttl_data += f'    rdf:label "{item["nama_peristiwa"]}" ;\n'
    ttl_data += f'    ex:tahun_peristiwa "{item["tahun_peristiwa"]}"^^xsd:integer ;\n'
    ttl_data += f'    ex:latitude "{item["latitude"]}"^^xsd:decimal ;\n'
    ttl_data += f'    ex:longitude "{item["longitude"]}"^^xsd:decimal .\n\n'

with open('indonesian-history.ttl', 'w') as f:
    f.write(ttl_data)
