"""
 Created by Tang on 2020/2/11 12:00
"""

from flask import jsonify, request, json, render_template, flash
from flask_login import current_user

from app.forms.book import SearchForm

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from ..models.base import db
from ..models.book import Book
from ..models.gift import Gift
from ..models.wish import Wish
from ..view_models.book import BookViewModel, BookCollection
from ..view_models.trade import TradeInfo


@web.route('/book/search')
def search():
    """
        q:普通关键字  isbn
        page
        ?q=..&page=1
    """

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip() #从form中取值，，strip（）去前后空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)

        # return json.dumps(result), 200, {'content-type':'application/json'}
    else:
        flash('搜索的关键字不符合要求，请重新输入')
    for book in books.books:
        a = Book.query.filter_by(isbn=book.isbn).first()
        if a is None :
            with db.auto_commit():
                booka = Book()
                booka.isbn = book.isbn
                booka.title = book.title
                booka.author = book.author
                booka.binding = book.binding
                booka.publisher = book.publisher
                booka.price = book.price
                booka.pages = book.pages
                booka.pubdate = book.pubdate
                booka.pages = book.pages
                booka.image = book.image
                booka.summary = book.summary
                db.session.add(booka)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False


    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        # 如果未登录，current_user将是一个匿名用户对象
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html',
                           book=book,
                           wishes=trade_wishes_model,
                           gifts=trade_gifts_model,
                           has_in_gifts = has_in_gifts,
                           has_in_wishes=has_in_wishes)





