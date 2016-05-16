# scrapzor
##Simple scrappy spider which collects ad information(Thailand, Pattaya real estate objects) and downloads images from each real estate ad.


**Project features:**


1. Async HTTP requests. You can send requests async. That means that you are sending requests before you will recieve response from previous requests sent.
2. Easy-to-manage spider scope(site sections to scrap) set
3. Downloads each ad images to hard drive

#####Item sample output in json format
```
{
    "category": "for_sale",
    "sku": "SRH7320",
    "hash": "79132b3eae1f633d230d3c8df02a0e87",
    "description": "\nBaan Suay Mai Ngam. This property is a 2 bedroom, 3 bathroom house available for rent in the east Pattaya area. It sits on a 51 sq.wah land plot (204 sq.metres) and is offered fully fitted and fully furnished\n\u00a0\nThere is a small garden to the front of the house and an outdoor sitting area. Inside there is a fitted European kitchen, an open plan layout, TV\u2019s and air conditioning throughout.\n\u00a0\nThis property can be rented with a minimum 6 month contract and a 2 month security deposit before move in\nTitle deed is held under Thai Company name.",
    "title": "Baan Suay Mai Ngam House For sale and for rent in East Pattaya",
    "url": "http://www.thaiproperty.com/for_sale/houses/pattaya/East-Pattaya/Baan-Suay-Mai-Ngam-_7320.html",
    "bedrooms": "2",
    "features": ["For Sale or Rent", "Fully Furnished", "European Kitchen", "Long Term Only", "In Company Name", "Fully Air Conditioned", "Cable TV"],
    "location": "East Pattaya",
    "isRented": false,
    "price_rent": "15000",
    "bathrooms": "3",
    "gps": {
        "lat": "12.889209747314453",
        "long": "100.911361694335940"
    },
    "type": "house",
    "price_sale": "2600000",
    "files": [{
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73201.jpg",
        "path": "full/ca815a43ff81d8512aa17e6254fbf9257f77acdf.jpg",
        "checksum": "1a4f75ec758ba6963d0be67a5eceb6ec"
    }, {
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-732011.jpg",
        "path": "full/8b17916bc089d2f242ca8de6e4b22469e774aff4.jpg",
        "checksum": "35cc0635d9c7b3f00c60acc18f619c62"
    }, {
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73204.JPG",
        "path": "full/457163b53d2514a9a7023a66246796a6c0369468.JPG",
        "checksum": "df9dd8b4d052c405b6f0465ee0eaa2c6"
    }, {
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-7320.JPG",
        "path": "full/f34325ccb2bff4d801e3e312799be97186df5511.JPG",
        "checksum": "057eb4b287c221289897f8337aac9691"
    }, {
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73209.JPG",
        "path": "full/310f7a7d254abbf121a754ba1353c32cfaae67e0.JPG",
        "checksum": "34857fe96f6a79a188550181b27aed41"
    }, {
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73206.JPG",
        "path": "full/d5ef38f41c3e490f9749ca5f5acb615c73aa0e87.JPG",
        "checksum": "d8a1670638f788766c592bdbbae74ae4"
    }, {
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73208.jpg",
        "path": "full/24d7dba0eb910666da6fa31e6ff1535e38f67c68.jpg",
        "checksum": "ff4cf4ab19090982c249b1f770f12be4"
    }, {
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-732010.JPG",
        "path": "full/f3cad0147dbbc0a9629d3c3bb3405db2b720ae3a.JPG",
        "checksum": "713864bbbcd2929a3f8123d8e48cb6c2"
    }, {
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73203.JPG",
        "path": "full/c315c30e07581cc107ff4ded5f055622dc8c7513.JPG",
        "checksum": "ae4e7d38681c7d46e384ab1f84ffbb12"
    }, {
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73202.JPG",
        "path": "full/206f33576bb83e6c22bd7e564bd66d242bff4d63.JPG",
        "checksum": "2c4faad1457915ce3f26a4a3a8f815c6"
    }, {
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-732012.JPG",
        "path": "full/253694cce1a672c2e74ea87747024567c3308d9a.JPG",
        "checksum": "10061efe35772b5cc2d913e1413e0a4c"
    }, {
        "url": "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73207.JPG",
        "path": "full/126a809e35f0d486d3179b6d87dd6f7408619fc5.JPG",
        "checksum": "e1a6d4ff6608d2e6006b0e740536ac2b"
    }],
    "file_urls": ["http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73201.jpg", "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-732011.jpg", "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73204.JPG", "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-7320.JPG", "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73209.JPG", "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73206.JPG", "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73208.jpg", "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-732010.JPG", "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73203.JPG", "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73202.JPG", "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-732012.JPG", "http://www.thaiproperty.com/public/uploads/images/Baan_Suay_Mai_Ngam_-73207.JPG"]
}
    ```

__Me gusta!__
