import pandas as pd
import matplotlib.pyplot as plt
import sys

#Load original dataset
df = pd.read_csv ('Q1_data.csv')

#print(df['order_amount'].mean()) #3045

analysis_type=0
if len(sys.argv)>1: analysis_type= int(sys.argv[1])

print()
print('Performing analysis type=',analysis_type)
print()

#Adding flags or quantities using already-existing data
df['is_biz_like'] = df['total_items']>10
df['per_item_amount'] = df['order_amount']/df['total_items']
df['is_rare'] = df['per_item_amount']>1000

#Apply selection
df_selected = df
#df_selected = df[df['order_amount']<10e3]
df_selected = df_selected[(df_selected['is_biz_like']==0) & (df['is_rare']==0)]
#df_selected = df_selected[df_selected['is_biz_like']==1]
#df_selected = df_selected[df_selected['is_rare']==1]
#df_selected = df_selected[(df_selected['is_biz_like']==1) | (df['is_rare']==1)]

# print(df_selected) # print entire dataset
print('AOV=',df_selected['order_amount'].mean())

# order_amount
if analysis_type==0:
    print('sigma=',df_selected['order_amount'].std())
    df_selected['order_amount'].hist(bins=50)
    plt.xlabel('order_amount')
    pass

# per_item_amount
elif analysis_type==1:
    df_selected=df_selected.drop_duplicates(subset='shop_id')
    print(df_selected)
    print('mean,sigma(per_item_amount)=',df_selected['per_item_amount'].mean(),df_selected['per_item_amount'].std(), 'count=',df_selected['per_item_amount'].count())
    df_selected['per_item_amount'].hist(bins=25)
    plt.xlabel('per_item_amount')
    pass
# transaction amount per payment method
elif analysis_type==2:
    df_selected[df_selected['payment_method']=='cash'       ]['order_amount'].hist(bins=20,histtype='step',range=[0,2000] )
    df_selected[df_selected['payment_method']=='debit'      ]['order_amount'].hist(bins=20,histtype='step',range=[0,2000] )
    df_selected[df_selected['payment_method']=='credit_card']['order_amount'].hist(bins=20,histtype='step',range=[0,2000] )
    print(df_selected[df_selected['payment_method']=='cash'       ]['order_amount'].mean())
    print(df_selected[df_selected['payment_method']=='debit'      ]['order_amount'].mean())
    print(df_selected[df_selected['payment_method']=='credit_card']['order_amount'].mean())
    labels= ['cash','debit','credit_card']
    plt.legend(labels)
    plt.xlabel('order_amount for payment_method')
    pass

# total_items/order
elif analysis_type==3:
    df_selected['total_items'].hist(bins=16)
    plt.xlabel('total_items/order')
    print('mean,sigma(total_items)=',df_selected['total_items'].mean(),df_selected['total_items'].std())
    pass

# Number of orders/customer
elif analysis_type==4:
    print(df_selected['user_id'].value_counts())
    print('mean, std(orders/customer)=',df_selected['user_id'].value_counts().to_numpy().mean(), df_selected['user_id'].value_counts().to_numpy().std() )
    plt.hist(df_selected['user_id'].value_counts().to_numpy(),bins='auto')
    plt.xlabel('Number of orders/customer')
    pass

# total_amount/customer
elif analysis_type==5:
    print(df_selected.groupby(['user_id']).sum())
    df_selected.groupby(['user_id']).sum()['order_amount'].hist(bins=50)
    print('mean,std(sum_order_amount)=',df_selected.groupby(['user_id']).sum()['order_amount'].mean(),df_selected.groupby(['user_id']).sum()['order_amount'].std())
    plt.xlabel('amount/customer')
    pass

else:
    print()
    print('analysis_type',analysis_type,'is not supported, please check the code...')
    print()
    pass

plt.show()
