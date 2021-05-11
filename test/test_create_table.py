from dao.create_table import Table

if __name__ == '__main__':
    # Table().create_table('bbbee')
    t = Table('bbbee')
    r = t.select_all()
    print(r)

    # insert
    row = {
        'stdSpciesNewCode':'',
        'delngDe':'',
        'price':''
    }

    t.insert(row)

