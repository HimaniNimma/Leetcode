select email from Person 
GROUP BY email
HAVING count(email)>1