class lib:
    book_dict = {"The Alche": 4, "1984": 3, "The 3 Mistake of my life": 2}

    def __init__(self, sname, sphoneno, email, sid, sadd, sbook=[]):
        self.sname = sname
        self.sphoneno = sphoneno
        self.email = email
        self.sid = sid
        self.sadd = sadd
        self.sbook = sbook

    def dis_obj(self):
        print(self.sname, self.sphoneno, self.email, self.sid, self.sadd, self.sbook)

    def issue_book(self):
        bn = input("Enter The Book: ")
        if bn in self.book_dict and self.book_dict_dict[bn] > 0:
            self.sbook += [bn]
            self.book_dict[bn] -= 1
        else:
            print("NA")

    def return_book(self):
        bn = input("Enter The Return Book: ")
        self.sbook.remove(bn)
        self.book_dict[bn] += 1


nasir = lib("nasir", 9237432434, "imamnasir73@gmail.com", 11, "sec-62")
print(lib.book_dict)
nasir.dis_obj()
nasir.issue_book()
nasir.dis_obj()
print(lib.book_dict)
nasir.return_book()

"""
in python we work on real time senarious using OOPS or in the presence of
class and object but OOPS follow some fundamentls
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

1. Encapsulation :- I. It is a phenomena where you bind the data, Method, Variable
            in a single Unit
            II. We Use encapsulation by hiding internal details of class and
            only expose the details which is neccessry using Access Specifier
            III. It is help to protect importent data for being changed directly
            and to keep data safe and organised 💊
            IV. We have three type of access specifir
                    1.Public
                    2.Protector
                    3.Private
                
                Public:- There are the Access Specifier Which are use in common
                        programing where anybody can access inside the class,
                        outside the class
                
                Protector:- Its a Access specifier where you give security to 
                        variable and method in the form of semi-security using
                        single underscore(_) 
                
                Private:- Its a most efficient Access specifier where you give 
                        complete secuity to class and objects for complete security
                        we user double underscore (__)eg - ATM Pins, Passwords
                        syntex -- class - c_name._c_name__attribute
                                 obj - ob_name._cname__attribute
                                 method - ob_name._cname__m_name()
                
                Modify:- 

Inheritance:- its a phenomena where one class deviate(share) its property to 
                another class, the class which deviate its property is known as
                parent class the class which accurie is known as child class
                
                C1 - Parent Class / Super Class
                C2 - Child / dirived / sub

                we have 5 type of in inheritance
                1.Single level inheritance
                2.Multiple inheritance
                3.Multi Level inheritance
                4.Hirarical inheritance
                5.Hybrid inheritance

                1.Single level inheritance:- in this inheritance parent deviate(share)
                    its property to child class
                    class A:
                        statement
                    class B(A):
                        statement

                        
            Constructor chaining:- it is a phenomena where we debiate(share) the 
                constructor of parent class inside the child class using super() method

                2.Multi Level inheritance:- #in this inheritance parent deviate (share)
                    its propertiy to child class in multiple phases

                    #its a downword directional model where lower class or last class carry the 
                    properties of all the above class
                    class A:
                        statement
                    class B(A):
                        statement
                    class C(B):
                        statement

                3.Multiple Inheritance:- its a inheritance where multiple parent
                    deviate(share) their properties to a single child class

                    its a hypothetical model where sometimes its work sometime not
                    work because of dynamic in nature

                    class A:
                        statement
                    class B:
                        statement
                    class C(A,B):
                        statement

                4.Hirarical inheritance:- in this inheritance single parent deviate(share)
                    its property to multiple child class

                    class A:
                        statement
                    class B(A):
                        statement
                    class C(A):
                        statement
                        
                5.Hybrid inheritance:- Its a inheritance where we have more then one model in a
                    in a single model that model is known as hybrid model

                    it is more efficent, effective model in inheritance


polymorphism:- It is a phenomena where we have one interface for with multiple implimentation
                for a perticulaer operation

                in this due to same name the other operation will over write the first operation

                we have three types of polymorphism 
                1.Method overloading
                2.Method overriding
                3.Operatior overloading

                    
 """
