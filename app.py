from flask import Flask,redirect,render_template,Response,flash,request,url_for,jsonify
from sqlcon import email_auth,authentication,registration,shop_bakery,dairy_data,grocey_data,popular_prods,dairy_prods,fresh_vegi,add_produc
import os
import Checksum
from werkzeug.utils import secure_filename

app = Flask(__name__)
MERCHANT_KEY = 'txD2tlHax&ls%3pt'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
UPLOAD_FOLDER = 'static/backend/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
global checksum

@app.route('/')
def home():
    return render_template('page-login.html')
@app.route('/home')
def home1():
    popular = popular_prods()
    dairy = dairy_prods()
    dod = fresh_vegi()
    
    return render_template('index.html',popular=popular,dairy=dairy,dod=dod)

@app.route('/page_about')
def page_about():
    return render_template('page-about.html')

@app.route('/page-contact')
def page_contact():
    return render_template('page-contact.html')
@app.route('/page-terms')
def page_terms():
    return render_template('page-terms.html')
@app.route('/shop-cart')
def shop_cart():
    return render_template('shop-cart.html')



@app.route('/vendors-list')
def vendors_list():
    return render_template('vendors-list.html')


@app.route('/blog-category-big')
def blog_category_big():
    return render_template('blog-category-big.html')
@app.route('/page_privacy_policy')
def page_privacy_policy():
    return render_template('page-privacy-policy.html')




@app.route('/shop-veg')
def shop_veg():
    d_data = fresh_vegi()
    return render_template('shop-veg.html',bdata=d_data)
@app.route('/shop-grocey')
def shop_grocey():
    d_data = grocey_data()
    return render_template('shop-grocey.html',bdata = d_data)
@app.route('/shop-dairy')
def shop_dairy():
    d_data = dairy_data()
    return render_template('shop-dairy.html',bdata = d_data)
@app.route('/shop-bakery')
def shop_bac():
    b_data = shop_bakery()
    

    return render_template('shop-bakery.html',bdata = b_data)
@app.route('/shop-meat')
def shop_meat():
    return render_template('shop-meat.html')

@app.route('/page-login')
def page_login():
    return render_template('page-login.html')
@app.route('/page-register')
def page_register():
    return render_template('page-register.html')

@app.route('/page-register',methods = ['GET','POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    password1 = request.form.get('password1')
    if(password==password1):
        resp = registration(username,email,password)
        if(resp>0):
            flash("Registration successfully!")
            return redirect(url_for('page_login'))
    else:
        return render_template('page-register.html')





######## authentication##########


@app.route('/email',methods = ['GET','POST'])
def email():
    email = request.form.get('email')
    if email!=0:

        e = email_auth(email)
        print(e)
        if e==0:
            flash("Email Insert successfully!",'success')
            return redirect(url_for('home'))
        else:
            flash('Email Aready Added Or Something Went Wrong!','error')
            return redirect(url_for('home'))
    else:
            flash('Something Went Wrong!','error')
            return redirect(url_for('home'))
    

@app.route('/login',methods = ['GET','POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    success = authentication(email,password)
    print(success)
    if(len(success)>0):
            popular = popular_prods()
            dairy = dairy_prods()
            dod = fresh_vegi()
        
            return render_template('index.html',popular=popular,dairy=dairy,dod=dod)

    else:
        return render_template('page-login.html')
    



@app.route('/admin')
def admin():
    return render_template('/backend/index.html')
@app.route('/page-products-list')
def page_products_list():
    return render_template('/backend/page-products-list.html')
@app.route('/page-orders-1')
def page_orders_1():
    return render_template('/backend/page-orders-1.html')
@app.route('/page-sellers-cards')
def page_sellers_cards():
    return render_template('/backend/page-sellers-cards.html')
@app.route('/page-form-product-1')
def page_form_product_1():
    return render_template('/backend/page-form-product-1.html')
@app.route('/page-transactions-1')
def page_transactions_1():
    return render_template('/backend/page-transactions-1.html')
@app.route('/page-reviews')
def page_reviews():
    return render_template('/backend/page-reviews.html')
@app.route('/page-brands')
def page_brands():
    return render_template('/backend/page-brands.html')
@app.route('/page-account-register')
def page_account_register():
    return render_template('/backend/page-account-register.html')
@app.route('/page-settings-1')
def page_settings_1():
    return render_template('/backend/page-settings-1.html')



@app.route('/product_add',methods=['GET','POST'])
def product_add():
    title = request.form.get("title")
    
    
    price = request.form.get("price")
    p_price = request.form.get("p_price")
    # Category = request.form.get("cat")
    Category = request.form['cat']
    sub_Category = request.form.get("sub-cat")
    # print(Category,title,price,p_price)
    file = request.files['file']
    if(file):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filedic = 'backend/images/'+filename
        resp = add_produc(title,price,p_price,Category,sub_Category,filedic)
        # c = ['Vegetables','Grocery','Dairy','Bakery','Meat']
        # for i in c:
        #     if(i==Category):
        # print(resp)

    
        if(resp==1):
            flash('Your data successfully !','success')
            return redirect(url_for('page_form_product_1'))
    
        else:


            return 'not done '


@app.route('/start/<order_id>/<price>',methods=['GET'])
def start(order_id,price):
    param_dict = {

                'MID': 'obQIPX90562701803310',
                'ORDER_ID': str(order_id),
                'TXN_AMOUNT': str(price),
                'CUST_ID': 'pradeepsaindi@gmail.com',
                'INDUSTRY_TYPE_ID': 'WEBSTAGING',
                'WEBSITE': 'Retail',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:5000/paymentstatus',

        }
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
    return render_template('paytm.html', param_dict= param_dict)

@app.route('/paymentstatus',methods=['GET','POST'])
def paymentstatus():
    # paytm will send you post request here
    form = request.form.to_dict()
    print(form)
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
            
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render_template('paymentstatus.html', response= response_dict)


if __name__ == '__main__':
    app.run(debug=True)