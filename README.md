## JBD first week project: Product class

### 1.day tasks

1. Product, Book, Electronic və Clothes klasları yaradılmalıdır.
3. Book, Electronic və Clothes klasları Product klasından varislik almalıdır.
4. Book klasının id, title, author, published_at, page_count, rating, price (qiymət), prod_cost (maya dəyəri), discount_price (endirimli qiymət), language, description, image, genre, publisher, category dəyişənləri olmalıdır.
5. Clothes klasının id, title, brand, size, category, rating, price (qiymət), prod_cost (maya dəyəri), discount_price (endirimli qiymət), color, description, image, material dəyişənləri olmalıdır.
6. Bu dəyişənlərin hansıların Product klasında hansıların Book və Clothes klaslarında olacağına siz qərar verməlisiniz. Ən optimal şəkildə yazılmalıdır.
7. discount_price dəyişəni obyekt yaradılanda price-ın dəyərinə bərabər olmalıdır.
8. set_discount_price(disc_type, disc_value) metodu olmalıdır. Bu metod hər klas üçün eyni şəkildə işləyəcək. İki dəyişən qəbul edəcək (disc_type, disc_value). disk_type 'faiz' sözüdürsə məhsulun dəyəri disc_value-dəki qədər faiz azaldılaraq discount_price-a yazılmalıdır. disk_type 'vahid' sözüdürsə məhsulun dəyəri disc_value-dəki qədər azaldılaraq discount_price-a yazılmalıdır. disk_type fərqli bir söz olarsa funksiya error mesajı qaytarmalı və obyektdə heç bir dəyişiklik etməməlidir.
9. id, prod_cost və price fildlərinə birbaşa çatmaq mümkün olmamalıdır. (Encapsulation)
10. prod_cost və price fildlərinə qiymət set və get metodları vasitəsi ilə yazılıb oxunmalıdır.
11. id fildinə məlumat yazılmamalıdır, sadəcə oxumaq imkanı olmalıdır. (id fildinə məlumat sadəcə obect yaradılanda yazılmalıdır)
12. Klasların xaricində get_name(obyekt) funksiyası olmalıdır. get_name(obyekt) funksiyasının qəbul etdiyi obyekt Book klasının obyektidirsə bu funksiya 'kitabın adı | kitabın yazarı' şəklində bir strinq qaytarmalıdır, funksiyasının qəbul etdiyi obyekt Clothes klasının obyektidirsə bu funksiya 'title | color' şəklində dəyər qaytarmalıdır. Əgər heç birinə aid deyilsə obyektin title fieldini qaytarmalıdır. (Polymorphism)
13. Yuxarıdakı klaslardan əlavə Electronic, Phone, Notebook klasları yaradın.
14. Electronik klası Product-dan varislik almalıdır. Phone və Notebook klasları isə Electronik klasından varislik almalıdır.
15. Bu 3 klasın dəyişənlərini və metodlarını özünüz təyin edin. Fildləri ən optimal şəkildə bölüşdürün və yuxarıdakı funksiyanallıqlar bu klaslarda da olmalıdır.

### 1.day questions

1. Yuxarıdakı tasklarda nə üçün Inheritance istifadə etdiniz? Bunun nə kimi avantajı olacaq?
2. 6 və 13-cü tasklarda fieldləri niyə o şəkildə paylaşdırdığınızı öz sözlərinizlə açıqlayın?
3. Sizcə biz Encapsulation-ı nə üçün istifadə etdik?
4. 12-ci taskda Polymorphism istifadə etmək bizə nə qazandırdı?


Kodları main.py faylına, sualların cavablarını answers.txt faylına yazın. Uğurlar!!!
