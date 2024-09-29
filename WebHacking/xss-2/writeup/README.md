1. Cookie dikeep di machine dari dreamhack, bisa diambil pake xss di post /flag. 
![alt text](image.png)
![alt text](image-1.png)

2. Bisa command injection pake <svg onload="location.href= '/memo?memo=' + document.cookie">. bakal ngeakses /memo dengan args memo=document.cookie, itu bakal ngeretrive cookie dan append ke variable global memo
![alt text](image-2.png)

3. flag bisa diakses dari bagian /memo dan udah ada di variable global memo