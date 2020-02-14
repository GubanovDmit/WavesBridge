# -*- coding: utf-8 -*- 
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import indexForm
import pywaves as pw
import traceback
import sys
import base58
import pywaves.crypto as crypto
nodeH = "http://dev-node-aws-fr-3.wavesnodes.com:6869"
nodeU = "http://dev-node-aws-fr-4.wavesnodes.com:6869"
tokenPortAddressH = "3HLCqQ8rJaceQSFxvrAKRc2AniLhXJDVHEG"
tokenPortAddressU = ""
@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    form = indexForm()
    if form.validate_on_submit():
        try:
            direction = form.direction.data
            node = nodeH if direction == "fromHtoU" else nodeU
            chain_id = 'H' if direction == "fromHtoU" else "U"
            tokenPortAddress = tokenPortAddressH if direction == "fromHtoU" else tokenPortAddressU
            pw.setNode(node, "", chain_id)
            myAddress = pw.Address(seed=form.seed.data)
            recepientInOtherChain = pw.Address(form.recepient.data)
            recepient = pw.Address(tokenPortAddress)
            amount = int(form.amount.data)
            atch =  crypto.bytes2str(base58.b58decode(recepientInOtherChain.address))
            print(atch)
            tx = myAddress.sendWaves(recepient, amount,attachment = atch)
            flash('txId= {}'.format(tx))
            #return redirect('/index')
        except:
            tb = traceback.format_exc()
            flash(tb)

    return render_template('index.html', title='Bridge', form=form)