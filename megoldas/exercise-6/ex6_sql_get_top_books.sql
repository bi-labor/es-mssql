select top 10 Books.ISBN, "Book-Title", "Book-Author", "Year-Of-Publication", "Image-URL-M", avg(Cast("Book-Rating"as decimal(38,8))) as rating_avg
from Books inner join Ratings on Books.ISBN = Ratings.ISBN
GROUP BY Books.ISBN,  "Book-Title", "Book-Author", "Year-Of-Publication", "Image-URL-M"
HAVING COUNT("Book-Rating") >=20
order by rating_avg desc