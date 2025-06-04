from database.DB_connect import DBConnect
from model.store import Store
from model.ordine import Ordine

class DAO():
        @staticmethod
        def getStore():
            conn = DBConnect.get_connection()

            cursor = conn.cursor(dictionary= True)

            result = []

            query = """select *
from stores s """


            cursor.execute(query)

            for row in cursor :
                result.append(Store(**row))

            cursor.close()

            conn.close()

            return result

        @staticmethod
        def getNodi(store):
            conn = DBConnect.get_connection()

            cursor = conn.cursor(dictionary=True)

            result = []

            query = """select distinct o.order_id as ord 
from orders o , order_items oi 
where o.store_id = %s
and o.order_id = oi.order_id """

            cursor.execute(query, (store, ))

            for row in cursor:
                result.append(row["ord"])

            cursor.close()

            conn.close()

            return result

        @staticmethod
        def getOrdini():
            conn = DBConnect.get_connection()

            cursor = conn.cursor(dictionary=True)

            result = []

            query = """select *
from orders o"""

            cursor.execute(query)

            for row in cursor:
                result.append(Ordine(**row))

            cursor.close()

            conn.close()

            return result


        @staticmethod
        def getArchi(store1, store2, k):
            conn = DBConnect.get_connection()

            cursor = conn.cursor(dictionary=True)

            result = []

            query = """select o1.order_id as id1 , o2.order_id as id2, sum(o1.quantity + o2.quantity) as peso
        from (select o.order_id , o.order_date , oi.product_id, oi.quantity
        from orders o , order_items oi 
        where o.store_id = %s
        and o.order_id = oi.order_id ) o1 , 
        (select o.order_id , o.order_date , oi.item_id, oi.quantity
        from orders o , order_items oi 
        where o.store_id = %s
        and o.order_id = oi.order_id ) o2 
        where o1.order_id != o2.order_id
        and ABS(datediff(o1.order_date , o2.order_date)  ) < %s
        and o1.order_date > o2.order_date
        group by o1.order_id , o2.order_id"""

            cursor.execute(query, (store1,store2,k, ))

            for row in cursor:
                result.append(row)

            cursor.close()

            conn.close()

            return result

