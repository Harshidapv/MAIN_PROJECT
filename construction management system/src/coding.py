import os
from  flask import*
from werkzeug.utils import secure_filename
from src.nlp import *

from src.dbconnection import *
app= Flask (__name__)
app.secret_key="hjgjkhgj"


app=Flask(__name__)
app.secret_key="eeeee"

import functools

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return render_template('loginindex.html')
        return func()

    return secure_function


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



@app.route('/')
def log():
    return  render_template("loginindex.html")

@app.route('/logincode',methods=['post','get'])
def logincode():
    un=request.form['textfield']
    ps=request.form['textfield2']
    qry="select * from login where username=%s and password=%s"
    val=(un,ps)
    res=selectone(qry,val)
    if res is None:
        return'''<script>alert("invalid");window.location='/'</script>'''
    elif res['type']=="admin":
        session['lid']=res['lid']
        return redirect('/admin_home')
    elif res['type'] == "contractor":
        session['lid']=res['lid']
        return redirect('/contractor_home')
    elif res['type'] == "user":
        session['lid']=res['lid']

        return redirect('/user_home')
    elif res['type'] == "vendor":
        session['lid']=res['lid']

        return redirect('/vendor_home')
    elif res['type'] == "worker":
        session['lid']=res['lid']

        return redirect('/worker_home')
    else:
        return '''<script>alert("invalid");window.location='/'</script>'''

@app.route('/add_contractors', methods=['post'])
@login_required
def add_contractors():
    Fname=request.form['textfield']
    Lname = request.form['textfield2']
    Place = request.form['textfield3']
    Post = request.form['textfield4']
    Pin = request.form['textfield5']
    Email = request.form['textfield6']
    Phone= request.form['textfield7']
    Catogory = request.form['select']
    Username = request.form['textfield8']
    Password = request.form['textfield9']

    qry="insert into login values(NULL,%s,%s,'contractor')"
    val=(Username,Password)
    id=iud(qry,val)
    qry1="insert into contractor values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str (id),Fname,Lname,Place,Post,Pin,Email,Phone,Catogory)
    iud(qry1,val1)
    return '''<script>alert("Added successfully");window.location='managecontractor'</script>'''


# ==========================================ADMIN================================


@app.route('/managecontractor')
@login_required

def managecontractor():
    qry="SELECT * FROM `contractor`"
    res=selectall(qry)
    print(res)
    return  render_template("Admin/add&managecontractor ad.html",val=res)
@app.route('/delete_contractor')
@login_required

def delete_contractor():
    id=request.args.get("id")
    qry="DELETE FROM `login` WHERE `lid`=%s"
    iud(qry,id)
    qry1="DELETE FROM `contractor` WHERE `lid`=%s"
    iud(qry1,id)
    return '''<script>alert("Deleted");window.location='/managecontractor'</script>'''


@app.route('/addcon_add',methods=['post'])
@login_required

def addcon_add():
    return  render_template("Admin/addcon add.html")
@app.route('/edit_contractors')
@login_required

def edit_contractors():
    id=request.args.get('id')
    session['EC_id']=id
    qry="select * from contractor where `lid`=%s"
    res=selectone(qry,id)
    return render_template("Admin/edit_contractor.html",val=res)

@app.route('/edit_contractors_post', methods=['post'])
@login_required

def edit_contractors_post():
    Fname=request.form['textfield']
    Lname = request.form['textfield2']
    Place = request.form['textfield3']
    Post = request.form['textfield4']
    Pin = request.form['textfield5']
    Email = request.form['textfield6']
    Phone= request.form['textfield7']
    Catogory = request.form['select']

    qry1="UPDATE `contractor` SET `fname`=%s,`lname`=%s,`place`=%s,`post`=%s,`pin`=%s,`email`=%s,`phone`=%s,`catogory`=%s WHERE `lid`=%s"
    val1=(Fname,Lname,Place,Post,Pin,Email,Phone,Catogory,session['EC_id'])
    iud(qry1,val1)
    return '''<script>alert("edited successfully");window.location='managecontractor'</script>'''



@app.route('/admin_home')
@login_required

def admin_home():
    return  render_template("aindex.html")

@app.route('/complaint_ad')
@login_required

def complaint_ad():
   qry="SELECT `complaint`. *, `user`.`fname`,  `user`.`lname` FROM `user` JOIN `complaint` ON `user`. `lid` = `complaint`.`lid` WHERE reply= 'pending'"
   res=selectall(qry)
   return  render_template("Admin/complaint ad.html",val=res)


@app.route('/complaint_reply')
@login_required

def complaint_reply():
    id=request.args.get('id')
    session['cid']=id
    return render_template("Admin/complaint ad2.html")
@app.route('/send_reply' ,methods=['post'])
@login_required

def send_reply():
    reply=request.form['textfield']
    qry="UPDATE  `complaint` SET reply=%s WHERE coid=%s"
    val=(reply,session['cid'])
    iud(qry,val)
    return '''<script>alert("Reply Sent");window.location='complaint_ad'</script>'''



@app.route('/rating_ad')
@login_required

def rating_ad():
    qry="SELECT  `rating`.*,`user`.`fname`,`user`.`lname`,`contractor`.`fname`  AS Fname,`contractor`.`lname`AS Lname  FROM `user` JOIN `rating` ON `user`.`lid`=`rating`.`uid` JOIN `contractor` ON `contractor`.`lid`=`rating`.`cid`"
    res=selectall(qry)
    return  render_template("Admin/rating add.html",val=res)


@app.route('/viewfeedback')
@login_required

def viewfeedback():
    qry="SELECT  `feedback`.*,`user`.`fname`,`user`.`lname`,`contractor`.`fname`AS Fname,`contractor`.`lname`AS Lname  FROM `contractor` JOIN `feedback` ON `contractor`.`lid`=`feedback`.`cid` JOIN `user` ON `user`.`lid`=`feedback`.`lid`"
    res=selectall(qry)
    return  render_template("Admin/viewfeedback ad.html",val=res)

#========================================contracrtor=====================================
@app.route('/add_workers', methods=['post'])
@login_required

def add_workers():
    Fname=request.form['textfield']
    Lname = request.form['textfield2']
    Place = request.form['textfield3']
    Post = request.form['textfield4']
    Pin = request.form['textfield5']
    Email = request.form['textfield6']
    Phone= request.form['textfield7']
    Username = request.form['textfield8']
    Password = request.form['textfield9']

    qry="insert into login values(NULL,%s,%s,'worker')"
    val=(Username,Password)
    id=iud(qry,val)
    qry1="insert into worker values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str (id),session['lid'],Fname,Lname,Place,Post,Pin,Phone,Email)
    iud(qry1,val1)
    return '''<script>alert("Added successfully");window.location='manage_worker1'</script>'''
@app.route('/edit_workers')
@login_required

def edit_workers():
    id=request.args.get('id')
    session['EW_id']=id
    qry="select * from worker where `lid`=%s"
    res=selectone(qry,id)
    return render_template("contractor/edit_worker.html",val=res)
@app.route('/edit_workers_post', methods=['post'])
@login_required

def edit_workers_post():
    Fname = request.form['textfield']
    Lname = request.form['textfield2']
    Place = request.form['textfield3']
    Post = request.form['textfield4']
    Pin = request.form['textfield5']
    Email = request.form['textfield6']
    Phone = request.form['textfield7']
    qry1 = "UPDATE `worker` SET `fname`=%s,`lname`=%s,`place`=%s,`post`=%s,`pin`=%s,`email`=%s,`phone`=%s WHERE `lid`=%s"
    val1 = (Fname, Lname, Place, Post, Pin,Phone, Email, session['EW_id'])
    iud(qry1, val1)
    return '''<script>alert("edited successfully");window.location='manage_worker1'</script>'''
@app.route('/delete_worker')
@login_required

def delete_worker():
    id=request.args.get("id")
    qry="DELETE FROM `login` WHERE `lid`=%s"
    iud(qry,id)
    qry1="DELETE FROM `worker` WHERE `lid`=%s"
    iud(qry1,id)
    return '''<script>alert("Deleted");window.location='/manage_worker1'</script>'''



@app.route('/chatwithcontractor')
@login_required

def chatwithcontractor():
    qry = "SELECT `request_for_contr`.*,`user`.`fname`,`lname` FROM `user` JOIN `request_for_contr` ON `request_for_contr`.`uid`=`user`.`lid` WHERE `request_for_contr`.`cid`=%s"
    res = selectall2(qry, session['lid'])
    return  render_template("contractor/Chat with User.html",val=res)




@app.route("/chat2")
@login_required

def chatsp():
    pid=request.args.get('uid')
    # print(pid,"==============================")
    session['pid']=pid
    qry="SELECT * FROM `user` WHERE `lid`=%s"
    res=selectone(qry,pid)


    # print(res)


    qry="SELECT * FROM `chat` WHERE `from_id`=%s AND `to_id`=%s OR `from_id`=%s AND `to_id`=%s "
    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)
    print(res1)

    # print(res)

    fname=res['fname']
    lname=res['lname']
    return render_template("contractor/chat2.html",data=res1,fname=fname,lname=lname,fr=session['lid'])



@app.route('/send',methods=['post'])
@login_required

def sendchat():
    message=request.form['textarea']
    to_id = session['pid']
    from_id = session['lid']
    qry="insert into chat values(null,%s,%s,%s,CURDATE(),curtime())"
    val=(from_id,to_id,message)
    iud(qry,val)


    return redirect("chatss")
@app.route("/chatss")
@login_required

def chatss():
    pid=session['pid']
    qry="SELECT * FROM `user` WHERE `lid`=%s"
    res=selectone(qry,pid)
    qry="SELECT * FROM `chat` WHERE `from_id`=%s AND `to_id`=%s OR `from_id`=%s AND `to_id`=%s "
    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)
    fname=res['fname']
    lname=res['lname']
    return render_template("/contractor/chat2.html",data=res1,fname=fname,lname=lname,fr=session['lid'])


@app.route('/contractor_home')
@login_required

def contractor_home():
    return  render_template("contractor/contractor home.html")


@app.route('/manage_worker1')
@login_required

def manage_worker1():
    qry = "SELECT * FROM `worker` where worker.cid=%s "
    res = selectall2(qry,session['lid'])
    print(res)
    return  render_template("contractor/manage contractor.html",val=res)

@app.route('/manage_worker2',methods=['post'])
@login_required

def manage_worker2():
    return  render_template("contractor/manage worker.html")
@app.route('/manage_plan')
@login_required

def manage_plan():
    qry="SELECT `plan`.*,`request_for_contr`.`work` FROM `plan` JOIN `request_for_contr` ON `plan`.`req_id`=`request_for_contr`.`rcid` WHERE request_for_contr.`cid`=%s"
    res=selectall2(qry,session['lid'])
    return  render_template("contractor/manage_plan.html",val=res)
@app.route('/delete_plan')
@login_required

def delete_plan():
    id = request.args.get("id")
    qry = "DELETE FROM `plan` WHERE `pid`=%s"
    iud(qry, id)
    return '''<script>alert("Deleted");window.location='/manage_plan'</script>'''


@app.route('/upload_plan',methods=['post'])
@login_required

def upload_plan():
    qry="SELECT * FROM `request_for_contr` WHERE `cid`=%s AND `status`='accepted'"
    res=selectall2(qry,session['lid'])
    return  render_template("contractor/plan.html",val=res)


@app.route('/upload_plan2',methods=['post'])
@login_required

def upload_plan2():
    plan=request.form['textfield']
    Details=request.form['textfield2']
    Image=request.files['file']
    fn=secure_filename(Image.filename)
    Image.save(os.path.join('static/plan',fn))
    Work=request.form['select']
    qry="INSERT INTO`plan`VALUES(NULL,%s,%s,%s,%s,curdate(),%s,'pending')"
    val=(session['lid'],plan,Details,fn,Work)
    iud(qry, val)
    return '''<script>alert("Uploaded successfully");window.location='manage_plan'</script>'''

@app.route('/rating')
@login_required

def rating():
    qry = "SELECT  `rating`.*,`user`.`fname`,`user`.`lname`  FROM `user` JOIN `rating` ON `user`.`lid`=`rating`.`uid` "
    res = selectall(qry)
    return  render_template("contractor/rating con.html",val=res)

@app.route('/salary1')
@login_required

def salary1():
    qry="SELECT `salary`. *, `worker`.`fname`, `worker`.`lname` FROM `worker` JOIN `salary` ON `worker`.`lid` = `salary`.`wid` where worker.cid=%s  "
    res = selectall2(qry,session['lid'])
    print(res)
    return  render_template("contractor/salary1.html",val=res)
@app.route('/add_salary', methods=['post'])
@login_required

def add_salary():
    Workname=request.form['select']
    Salary = request.form['textfield']
    Days = request.form['textfield2']
    qry1 = "insert into `salary` values(NULL,%s,%s,%s)"
    val1 = (Workname,Salary,Days)
    iud(qry1, val1)
    return '''<script>alert("Added successfully");window.location="/salary1"</script>'''



@app.route('/salary2',methods=['post'])
@login_required

def salary2():
    qry="select * from `worker` where worker.cid=%s "
    res=selectall2(qry,session['lid'])
    print(res)
    return  render_template("contractor/salary2.html",val=res)
@app.route('/delete_salary')
@login_required

def delete_salary():
    id = request.args.get("id")
    qry = "DELETE FROM `salary` WHERE `sid`=%s"
    iud(qry, id)
    return '''<script>alert("Deleted");window.location='/salary1'</script>'''
@app.route('/edit_salary1')
@login_required

def edit_salary1():
    id = request.args.get('id')
    print(id)
    session['SC_id'] = id
    qry = "select * from salary where `sid`=%s"
    res = selectone(qry, id)
    return render_template("contractor/edit_salary.html", val=res)
@app.route('/edit_salary2')
@login_required

def edit_salary2():
    Workname = request.form['select']
    Salary = request.form['textfield']
    Days = request.form['textfield2']
    qry1="UPDATE `salary` SET `wid`=%s,`salary`=%s,`days`=%s WHERE `sid`=%s"
    val1 = (Workname,Salary,Days,session['SC_id'])
    iud(qry1, val1)
    return '''<script>alert("edited successfully");window.location='salary1'</script>'''
@app.route('/delete_sh')
@login_required

def delete_sh():
    id = request.args.get("id")
    qry = "DELETE FROM `shedule` WHERE `shed_id`=%s"
    iud(qry, id)
    return '''<script>alert("Deleted");window.location='/manage_plan'</script>'''
@app.route('/manage_shedule',methods=['post','get'])
@login_required

def manage_shedule():
    qry="SELECT * FROM `shedule` JOIN `request_for_contr` ON `request_for_contr`.`rcid`=`shedule`.`req_id` WHERE `request_for_contr`.`cid`=%s"
    res = selectall2(qry,session['lid'])
    return  render_template("contractor/manage_shedule.html",val=res)



@app.route('/schedule1',methods=['post','get'])
@login_required

def schedule1():
    qry="SELECT `request_for_contr`.*,`user`.`fname`,`lname` FROM `user` JOIN `request_for_contr` ON `request_for_contr`.`uid`=`user`.`lid` WHERE `request_for_contr`.`cid`=%s"
    res = selectall2(qry,session['lid'])
    return  render_template("contractor/schedule con.html",val=res)

@app.route('/schedule2')
@login_required

def schedule2():
    id = request.args.get('id')
    session['req_id'] = id
    return  render_template("contractor/schedule2.html")
@app.route('/add_schedule',methods=['post'])
@login_required

def add_schedule():
    From_date = request.form['date']
    To_date = request.form['date2']
    qry1 = "INSERT INTO `shedule`VALUES(NULL,%s,%s,%s,curdate(),'pending')"
    val1 = (session['req_id'],From_date , To_date,)
    iud(qry1, val1)
    return '''<script>alert("scheduled successfully");window.location='manage_shedule'</script>'''


@app.route('/workamount1')
@login_required

def workamount1():
    qry="SELECT * FROM `request_for_contr` WHERE `status`='accepted' AND `cid`=%s"
    res=selectall2(qry,session['lid'])
    return  render_template("contractor/update work amount1.html",val=res)

@app.route('/workamount2')
@login_required

def workamount2():
    id=request.args.get('id')
    session['Wrk_id']=id
    return  render_template("contractor/update work amount2.html")

@app.route('/workamount21',methods=['post'])
@login_required

def workamount21():
    amount = request.form['textfield']
    qry="INSERT INTO `work_amound` VALUES(NULL,%s,%s,CURDATE(),'pending')"
    val=(session['Wrk_id'],amount)
    iud(qry,val)
    return '''<script>alert("Added successfully");window.location='workamount1'</script>'''




@app.route('/view_assigned_work')
@login_required

def view_assigned_work():
    qry="SELECT `request_for_contr`.*,`worker`.`fname`,`worker`.`lname`,`assign`.`rcid`,assign.status as astatus FROM `request_for_contr` JOIN`assign`ON `assign`.`rcid`=`request_for_contr`.`rcid` JOIN `worker` ON `assign`.`wid`=`worker`.`lid` WHERE `request_for_contr`.`cid`=%s"
    res = selectall2(qry,session['lid'])
    return  render_template("contractor/view assigned works.html",val=res)

@app.route('/view_payment_details')
@login_required

def view_payment_details():
    qry="SELECT * FROM `request_for_contr` JOIN `work_amound` ON `work_amound`.`work_id`=`request_for_contr`.`rcid` JOIN `user`ON `user`.`lid`=`request_for_contr`.`uid` WHERE `request_for_contr`.`cid`=%s"
    res=selectall2(qry,session['lid'])
    return  render_template("contractor/view payment details.html",val=res)

@app.route('/view_product1')
@login_required

def view_product1():
    qry="SELECT * FROM `order` JOIN `order_details` ON `order`.`oid`=`order_details`.`oid` JOIN `product` ON `product`.`pid`=`order_details`.`pid`JOIN `stock` ON `stock`.`pid`=`product`.`pid`  WHERE `order`.`uid`=%s and order.status='cart'"
    res=selectall2(qry,session['lid'])
    qry1="    SELECT * FROM `order` WHERE  uid=%s AND `status`='cart'"
    res1=selectone(qry1,session['lid'])

    return  render_template("contractor/view product1.html",val=res,val1=res1)

@app.route('/view_order_status')
@login_required

def view_order_status():
    qry="SELECT * FROM `order` JOIN `order_details` ON `order`.`oid`=`order_details`.`oid` JOIN `product` ON `product`.`pid`=`order_details`.`pid`JOIN `stock` ON `stock`.`pid`=`product`.`pid`  WHERE `order`.`uid`=%s and order.status!='cart'"
    res=selectall2(qry,session['lid'])

    return  render_template("contractor/view_order_status.html",val=res)



@app.route('/user_pay_proceed', methods=['post','get'])
@login_required

def user_pay_proceed():
    import razorpay
    # amount = request.form['textfield']
    oid = request.args.get('id')
    session['OR_id'] = oid
    amount=request.args.get('id')
    session['pay_amount'] = amount
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': amount+"00", 'currency': "INR", 'payment_capture': '1'})
    qry = "select * from contractor where lid=%s"
    res = selectone(qry, session['lid'])
    return render_template('contractor/UserPayProceed.html', p=payment,val=res)



@app.route('/on_payment_success', methods=['post'])
@login_required

def on_payment_success():
    amt = session['pay_amount']
    qry = "INSERT INTO `payment` VALUES(NULL,%s,%s,CURDATE())"
    iud(qry, ( session['lid'], amt))
    qry1="UPDATE `order` SET `status`='payed' WHERE `oid`=%s"
    val=(session['OR_id'])
    iud(qry1,val)

    # qry = "UPDATE `charity_information` SET `amount`=`amount`-%s WHERE `id`=%s"
    # iud(qry, (amt,charity))

    return '''<script>alert("Success! Thank you for your Contribution");window.location="view_product3"</script>'''


@app.route('/order_now')
@login_required

def order_now():
    oid = request.args.get('id')
    qry1 = "UPDATE `order` SET `status`='ordered' WHERE `oid`=%s"
    iud(qry1, oid)
    return '''<script>alert("Ordered successfully");window.location='view_order_status'</script>'''




@app.route('/view_product2')
@login_required

def view_product2():
    id=request.args.get('id')
    session['PRO_id']=id
    qry="select * from product join `stock`on `stock`.`pid`=`product`.`pid` where product.pid=%s"
    res=selectone(qry,id)
    print(res)
    return  render_template("contractor/view product2.html",val=res)

# //////////////////////////////////////Addto cart////////////////////////////////////////////
@app.route('/add_to_cart', methods=['POST'])
@login_required

def add_to_cart():
    # pro_id=request.form['pro_id']
    qty=request.form['textfield5']
    print (qty,"QQQQQQQQQQQQQQQ")
    # lid=request.form['lid']

    qq="select * from `product` where `pid`=%s"
    rees=selectone(qq,session['PRO_id'])
    tt=int(rees['price'])*int(qty)
    qry123="SELECT * FROM`stock` JOIN `product` ON `product`.`pid`=`stock`.`pid` WHERE product.pid=%s"
    rees1=selectone(qry123,session['PRO_id'])
    stock=rees1['stock']
    print (stock,"SSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    nstk=int(stock)-int(qty)

    if int(stock)>=int(qty):

        up="update `stock` set `stock`=%s where `pid`=%s"
        iud(up,(nstk,session['PRO_id']))

        q="select * from `order` where `uid`=%s and `status`='cart'"
        res=selectone(q,session['lid'])

        if res is None:
            qry="insert into `order` values (null,%s,curdate(),%s,'cart')"
            val=(session['lid'],tt)
            id=iud(qry,val)
            qry1="insert into `order_details` values (null,%s,%s,%s)"
            va=(str(id),session['PRO_id'],qty)
            iud(qry1,va)
            return '''<script>alert("Add to cart");window.location='view_product1'</script>'''
        else:
            total=int(res['amount'])+int(tt)
            qry = "UPDATE `order` SET `amount`=%s WHERE `oid`=%s"
            val = (total, str(res['oid']))
            id = iud(qry, val)

            qry1="SELECT * FROM `order_details` WHERE `pid`=%s AND `oid`=%s"
            res12=selectone(qry1,(session['PRO_id'],str(res['oid'])))
            print(res12)
            if res12 is None:
                qry1 = "insert into `order_details` values (null,%s,%s,%s)"
                va = (str(res['oid']), session['PRO_id'], qty)
                iud(qry1, va)
            else:
                qry1 = "UPDATE `order_details` SET `qty`=%s WHERE `id`=%s"
                quty=int(res12['qty'])+int(qty)
                va = (quty,str(res12['id']))
                iud(qry1, va)
            return '''<script>alert("Add to cart");window.location='view_product1'</script>'''
    else:
        return '''<script>alert("out of stock");window.location='view_product3'</script>'''


@app.route('/view_product3')
@login_required

def view_product3():
    qry="select * from product"
    res=selectall(qry)
    return  render_template("contractor/view product3.html",val=res)


@app.route('/work_request1')
@login_required

def work_request1():
   qry="SELECT  `request_for_contr`. *, `user`.fname, `user`.lname  FROM `user`  JOIN `request_for_contr` ON `user`. `lid` = `request_for_contr`.`uid`"
   res = selectall(qry)
   return  render_template("contractor/workrequest con.html",val=res)

@app.route('/accept_contractor')
@login_required

def accept_contractor():
    id=request.args.get('id')
    qry1 = "UPDATE `request_for_contr` SET `status`='accepted' WHERE`rcid`=%s"
    iud(qry1,id)
    return '''<script>alert("Accepted");window.location='work_request1'</script>'''
@app.route('/rejected_contractor')
@login_required

def rejected_contractor():
    id=request.args.get('id')
    qry1 = "UPDATE `request_for_contr` SET `status`='rejected' WHERE`rcid`=%s"
    iud(qry1,id)
    return '''<script>alert("Rejected");window.location='work_request1'</script>'''
@app.route('/work_request2')
@login_required

def work_request2():
    qry="select * from worker"
    res=selectall(qry)
    id = request.args.get('id')
    session['rc_id'] = id
    return  render_template("contractor/workRequest con2.html",val=res)

@app.route('/assign_contractor',methods=['post'])
@login_required

def assign_contractor():
    worker=request.form['select']
    qry="INSERT INTO `assign` VALUES(NULL,%s,%s,CURDATE(),'Assigned')"
    val = (session['rc_id'],worker)
    iud(qry, val)

    qry1="UPDATE `request_for_contr` SET `status`='Assigned' WHERE`rcid`=%s"
    iud(qry1,session['rc_id'])
    return '''<script>alert("Assigned");window.location='work_request1'</script>'''


#===================================================USER===========================================================

@app.route('/chat_with_contractor')
@login_required

def chat_with_contractor():
    qry="SELECT contractor.lid, `contractor`.`fname`,`contractor`.`lname`,`request_for_contr`.* FROM `request_for_contr` JOIN `contractor` ON `contractor`.`lid`=`request_for_contr`.`cid` WHERE `request_for_contr`.`uid`=%s"
    res=selectall2(qry,session['lid'])
    return  render_template("user/chat with user.html",val=res)





# /////////////////////////////chat/////////////////////////////////////////////////////////////////

@app.route("/chat21")
@login_required

def chatsp1():
    pid=request.args.get('uid')
    # print(pid,"==============================")
    session['pid']=pid
    qry="SELECT * FROM `contractor` WHERE `lid`=%s"
    res=selectone(qry,pid)


    # print(res)


    qry="SELECT * FROM `chat` WHERE `from_id`=%s AND `to_id`=%s OR `from_id`=%s AND `to_id`=%s "
    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)
    # print(res1)

    # print(res)

    fname=res['fname']
    lname=res['lname']
    return render_template("user/chat2.html",data=res1,fname=fname,lname=lname,fr=str(session['lid']))



@app.route('/send1',methods=['post'])
@login_required

def sendchat1():
    message=request.form['textarea']
    to_id = session['pid']
    from_id = session['lid']
    qry="insert into chat values(null,%s,%s,%s,CURDATE(),curtime())"
    val=(from_id,to_id,message)
    iud(qry,val)


    return redirect("chatss1")
@app.route("/chatss1")
@login_required

def chatss1():
    pid=session['pid']
    qry="SELECT * FROM `contractor` WHERE `lid`=%s"
    res=selectone(qry,pid)
    qry="SELECT * FROM `chat` WHERE `from_id`=%s AND `to_id`=%s OR `from_id`=%s AND `to_id`=%s "
    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)
    print (res1)
    fname=res['fname']
    lname=res['lname']
    return render_template("/user/chat2.html",data=res1,fname=fname,lname=lname,fr=str(session['lid']))







# /////////////////////////////chat/////////////////////////////////////////////////////////////////

@app.route('/send_complaint1',methods=['post','get'])
@login_required

def send_complaint1():
    qry="SELECT * FROM `complaint` WHERE `lid`=%s"
    res=selectall2(qry,session['lid'])
    return  render_template("user/send complaint1.html",val=res)
@app.route('/send_complaint2',methods=['post','get'])
@login_required

def send_complaint2():
    return  render_template("user/send complaint2.html")


@app.route('/send_complaint21',methods=['post'])
@login_required

def send_complaint21():
    com=request.form['textfield']
    qry="INSERT INTO `complaint` VALUES(NULL,%s,%s,CURDATE(),'pending')"
    val=(com,session['lid'])
    iud(qry,val)
    return '''<script>alert("Sended ");window.location='send_complaint1'</script>'''

@app.route('/send_feedback1')
@login_required

def send_feedback1():
    qry="SELECT * FROM `contractor` "
    res=selectall(qry)
    return  render_template("user/send feedback1.html",val=res)
@app.route('/send_feedback12',methods=['post'])
@login_required

def send_feedback12():
    con=request.form['select']

    rating=request.form['select2']
    feed=request.form['textfield']
    emo=sent(feed)
    qry="INSERT INTO `feedback`VALUES(NULL,%s,%s,%s,CURDATE(),%s)"
    val=(con,session['lid'],feed,emo)
    iud(qry,val)
    qry1="INSERT INTO `rating`VALUES(NULL,%s,%s,%s,CURDATE())"
    val1=(session['lid'],con,rating)
    iud(qry1,val1)
    return '''<script>alert("Sended ");window.location='user_home'</script>'''





@app.route('/send_rating')
@login_required

def send_rating():
    return  render_template("user/send rating.html")

@app.route('/send_request_for_contractor1')
@login_required

def send_request_for_contractor1():
    qry="SELECT * FROM `contractor`"
    res=selectall(qry)
    return  render_template("user/send request for contractor1.html",val=res)


@app.route('/VIEW_REQUEST_STATUS')
@login_required

def VIEW_REQUEST_STATUS():
    qry="SELECT `request_for_contr`.*,`contractor`. `fname`,`lname`FROM `request_for_contr` JOIN `contractor` ON `contractor`.`lid`=`request_for_contr`.`cid` WHERE `request_for_contr`.`uid`=%s"

    res=selectall2(qry,session['lid'])
    return  render_template("user/VIEW_REQUEST_STATUS.html",val=res)


@app.route('/send_request_for_contractor2')
@login_required

def send_request_for_contractor2():
    id=request.args.get('id')
    session['cnid']=id
    return  render_template("user/send request for contractor2.html")

@app.route('/add_request_for_contractor',methods=['post','get'])
@login_required

def add_request_for_contractor():
    work=request.form['textfield']
    details=request.form['textfield2']
    qry="INSERT INTO `request_for_contr` VALUES (NULL,%s,%s,%s,%s,CURDATE(),'pending')"
    val=(session['lid'],session['cnid'],work,details)
    iud(qry,val)
    return '''<script>alert("Requested successfully");window.location='send_request_for_contractor1'</script>'''


@app.route('/user_home')
@login_required

def user_home():
    return  render_template("user/user home.html")

@app.route('/view_plan')
@login_required

def view_plan():
    qry="SELECT `contractor`.`fname`,`contractor`.`lname`,`request_for_contr`.* ,`plan`.*, plan.status as pstatus FROM `request_for_contr` JOIN `contractor` ON `contractor`.`lid`=`request_for_contr`.`cid` JOIN `plan` ON `plan`.`cid`=`contractor`.`lid` WHERE `request_for_contr`.`uid`=%s GROUP BY  pid "
    res=selectall2(qry,session['lid'])
    return  render_template("user/view plan.html",val=res)



@app.route('/accept_plan')
@login_required

def accept_plan():
    id=request.args.get('id')
    qry1 = "UPDATE `plan` SET `status`='Accepted' WHERE`pid`=%s"
    iud(qry1,id)
    return '''<script>alert("Accepted");window.location='view_plan'</script>'''

@app.route('/reject_plan')
@login_required

def reject_plan():
    id=request.args.get('id')
    qry1 = "UPDATE `plan` SET `status`='Rejected' WHERE`pid`=%s"
    iud(qry1,id)
    return '''<script>alert("Rejected");window.location='view_plan'</script>'''









@app.route('/view_time_schedule')
@login_required

def view_time_schedule():
    return  render_template("user/view  timeschedule.html")

#================================================VENDOR=============================================

@app.route('/add_and_manage_product1')
@login_required

def add_and_manage_product1():
    qry="SELECT * FROM `product` JOIN `stock` ON `stock`.`pid`=`product`.`pid` WHERE `vid`=%s"
    res = selectall2(qry, session['lid'])

    return  render_template("vendor/add &manage product1.html",val=res)










@app.route('/add_and_manage_product2',methods=['post'])
@login_required

def add_and_manage_product2():
    return  render_template("vendor/add &manage product2.html")
@app.route('/add_and_manage_product21',methods=['post'])
@login_required

def add_and_manage_product21():
    pname=request.form['textfield']
    im=request.files['file']
    fn = secure_filename(im.filename)
    im.save(os.path.join('static/product', fn))

    stock=request.form['textfield3']

    price=request.form['textfield4']
    qry="INSERT INTO `product` VALUES(NULL,%s,%s,%s,%s)"

    val=(pname,fn,price,session['lid'])
    id=iud(qry,val)
    qry1="INSERT INTO `stock` VALUES(NULL,%s,%s,CURDATE())"
    val1=(str(id),stock)
    iud(qry1,val1)

    return '''<script>alert("Added successfully");window.location='add_and_manage_product1'</script>'''


@app.route('/delete_product')
@login_required

def delete_product():
    id=request.args.get("id")
    qry="DELETE FROM `product` WHERE `pid`=%s"
    iud(qry,id)
    qry1="DELETE FROM `stock` WHERE `pid`=%s"
    iud(qry1,id)
    return '''<script>alert("Deleted");window.location='/add_and_manage_product1'</script>'''

@app.route('/edit_product')
@login_required

def edit_product():
    id=request.args.get("id")
    session['PID']=id
    qry="select  * from `product` WHERE `pid`=%s"
    res=selectone(qry,id)
    print (res )

    return  render_template("vendor/edit_product.html",i=res)

@app.route('/edit_product2',methods=['post'])
@login_required

def edit_product2():
    try:
        pname=request.form['textfield']
        im=request.files['file']
        fn = secure_filename(im.filename)
        im.save(os.path.join('static/product', fn))


        price=request.form['textfield4']
        qry="UPDATE `product` SET `pname`=%s,`image`=%s,`price`=%s WHERE `pid`=%s"

        val=(pname,fn,price,session['PID'])
        iud(qry,val)
    except:
        pname = request.form['textfield']
        # im = request.files['file']
        # fn = secure_filename(im.filename)
        # im.save(os.path.join('static/product', fn))

        price = request.form['textfield4']
        qry = "UPDATE `product` SET `pname`=%s,`price`=%s WHERE `pid`=%s"

        val = (pname, price, session['PID'])
        iud(qry, val)

    return '''<script>alert("Edited successfully");window.location='add_and_manage_product1'</script>'''






@app.route('/update_stock1')
@login_required

def update_stock1():
    qry="SELECT * FROM `product` JOIN `stock` ON `stock`.`pid`=`product`.`pid` WHERE `product`.`vid`=%s"
    res=selectall2(qry,session['lid'])
    return  render_template("vendor/update stock1.html",val=res)

@app.route('/update_stock2')
@login_required

def update_stock2():
    id=request.args.get('id')
    session['SK_id']=id
    return  render_template("vendor/update stock2.html")

@app.route('/update_stock21',methods=['post'])
@login_required

def update_stock21():
    stock=request.form['textfield']
    qry="UPDATE `stock` SET `stock`=%s WHERE `stid`=%s"
    val=(stock,session['SK_id'])
    iud(qry,val)
    return '''<script>alert("Edited successfully");window.location='update_stock1'</script>'''






@app.route('/vendor_home')
@login_required

def vendor_home():
    return  render_template("vendor/vendor home.html")

@app.route('/view_request_for_product')
@login_required

def view_request_for_product():
    qry="SELECT `contractor`.`fname`,`lname`, `product`.*,`order_details`.*,`order`.*,`order`.`oid` AS orid FROM `product` JOIN `order_details` ON `product`.`pid`=`order_details`.`pid` JOIN `order` ON `order`.`oid`=`order_details`.`oid` JOIN `contractor` ON `order`.`uid`=`contractor`.`lid` WHERE `product`.`vid`=%s AND `order`.`status`='ordered'"
    res=selectall2(qry,session['lid'])

    return  render_template("vendor/view request for product.html",val=res)

@app.route('/accept_order')
@login_required

def accept_order():
    id=request.args.get('id')
    qry1 = "UPDATE `order` SET `status`='Accepted' WHERE `oid`=%s"
    iud(qry1,id)
    return '''<script>alert("Accepted");window.location='view_request_for_product'</script>'''

@app.route('/Reject_order')
@login_required

def Reject_order():
    id=request.args.get('id')
    qry1 = "UPDATE `order` SET `status`='Rejected' WHERE `oid`=%s"
    iud(qry1,id)
    return '''<script>alert("Rejected");window.location='view_request_for_product'</script>'''


#=======================================WORKER===========================================

@app.route('/view_assigned_work_by_workers1')
@login_required

def view_assigned_work_by_workers1():
    qry="SELECT `assign`.`aid`,`request_for_contr`.`work`,`details`,`request_for_contr`.`rcid`,`contractor`.`fname`,`lname` FROM `contractor` JOIN `request_for_contr` ON `contractor`.`lid`=`request_for_contr`.`cid` JOIN `assign` ON `assign`.`rcid`=`request_for_contr`.`rcid` WHERE `assign`.`wid`=%s  and `assign`.`status`='Assigned'"
    res=selectall2(qry,session['lid'])
    print (session['lid'])
    print (res)
    return  render_template("Worker/view assigned work by workers.html",val=res)

@app.route('/view_assigned_work_by_workers2')
@login_required

def view_assigned_work_by_workers2():
    id=request.args.get('id')
    session['aid']=id
    return  render_template("Worker/view assigned work by workers2.html")
@app.route('/view_assigned_work_by_workers21',methods=['post'])
@login_required

def view_assigned_work_by_workers21():
    status=request.form['textfield']
    qry="UPDATE `assign` SET `status`=%s WHERE `aid`=%s"
    val=(status,session['aid'])
    iud(qry,val)
    return '''<script>alert("updated  successfully");window.location='view_assigned_work_by_workers1'</script>'''



@app.route('/view_salary')
@login_required

def view_salary():
    qry="SELECT * FROM `salary` WHERE `wid`=%s"
    res=selectall2(qry,session['lid'])
    return  render_template("Worker/view salary.html",val=res)


@app.route('/worker_home')
@login_required

def worker_home():
    return  render_template("Worker/worker home.html")



@app.route('/ratiview_time_scheduleng')
@login_required

def ratiview_time_scheduleng():
    qry="SELECT `request_for_contr`.`work`,`shedule`.* FROM `shedule`JOIN `request_for_contr` ON `shedule`.`req_id`=`request_for_contr`.`rcid` WHERE `request_for_contr`.`uid`=%s"
    res=selectall2(qry,session['lid'])
    return  render_template("user/view timeschedule.html",val=res)

@app.route('/accept_sh')
@login_required

def accept_sh():
    id=request.args.get('id')
    qry1 = "UPDATE `shedule` SET `status`='Accepted' WHERE `shed_id`=%s"
    iud(qry1,id)
    return '''<script>alert("Accepted");window.location='ratiview_time_scheduleng'</script>'''


@app.route('/reject_sh')
@login_required

def reject_sh():
    id=request.args.get('id')
    qry1 = "UPDATE `shedule` SET `status`='Reject' WHERE `shed_id`=%s"
    iud(qry1,id)
    return '''<script>alert("Reject");window.location='ratiview_time_scheduleng'</script>'''

@app.route('/view_work_amount')
@login_required

def view_work_amount():
    qry="SELECT * FROM `request_for_contr` JOIN `work_amound` ON `work_amound`.`work_id`=`request_for_contr`.`rcid` JOIN `contractor`ON `contractor`.`lid`=`request_for_contr`.`cid` WHERE `request_for_contr`.`uid`=%s"
    res=selectall2(qry,session['lid'])
    return  render_template("user/view_work_amount.html",val=res)

@app.route('/user_reg')
@login_required

def user_reg():
    return render_template("user_reg_index.html")


@app.route('/user_reg1',methods=['post','get'])
@login_required

def user_reg1():
    firstname=request.form['textfield']
    lastname=request.form['textfield2']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    phone=request.form['textfield6']
    email=request.form['textfield7']
    # latitude=request.form['textfield10']
    # longitude=request.form['textfield11']
    username=request.form['textfield8']
    password=request.form['textfield9']
    qry="INSERT INTO `login` VALUES (NULL,%s,%s,'user')"
    val=(username,password)
    id=iud(qry,val)
    qry1="INSERT INTO `user` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),firstname,lastname,place,post,pin,email,phone)
    iud(qry1,val1)
    return '''<script>alert("success");window.location="/"</script>'''

@app.route('/v_reg_index')
@login_required

def v_reg_index():
    return render_template("v_reg_index.html")


@app.route('/v_reg_index1',methods=['post','get'])
@login_required

def v_reg_index1():
    firstname=request.form['textfield']
    lastname=request.form['textfield2']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    phone=request.form['textfield6']
    email=request.form['textfield7']
    # latitude=request.form['textfield10']
    # longitude=request.form['textfield11']
    username=request.form['textfield8']
    password=request.form['textfield9']
    qry="INSERT INTO `login` VALUES (NULL,%s,%s,'vendor')"
    val=(username,password)
    id=iud(qry,val)
    qry1="INSERT INTO `vendor` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),firstname,lastname,place,post,pin,email,phone)
    iud(qry1,val1)
    return '''<script>alert("success");window.location="/"</script>'''







app.run(debug=True)