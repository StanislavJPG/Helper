from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from src.admin.service import AdminPanel
from src.auth.base_config import current_superuser
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Depends

from src.crud import update_book_args_by_admin, read_specific_book_from_database_by_admin, delete_redis_cache_statement
from src.database import RedisCash, get_async_session
from src.library.shemas import BookCreate


router = APIRouter(
    prefix='/api/admin_panel',
    tags=['admin_panel']
)


@router.post('/create_book', response_model=None, dependencies=[Depends(current_superuser)])
async def create_book_api(book: BookCreate, session: AsyncSession = Depends(get_async_session)):
    """
    This is function made for managing book
    that users wants to add to the cite
    """
    await update_book_args_by_admin(session=session, book=book)


@router.get('/search/{book_title}', dependencies=[Depends(current_superuser)], response_model=BookCreate)
async def search_specific_book_from_database_api(book_title: str,
                                                 session: AsyncSession = Depends(get_async_session)):
    book = await read_specific_book_from_database_by_admin(session=session, book_title=book_title)
    return book


@router.get('/', response_class=HTMLResponse, dependencies=[Depends(current_superuser)])
async def admin_panel_api(page: Optional[int] = 1, session: AsyncSession = Depends(get_async_session)):
    redis = RedisCash('admin_panel')

    if await redis.check():
        books_request = await redis.get()
    else:
        admin_panel_instance = await AdminPanel(page).get_users_requests(session=session)
        books_request = await redis.executor(data=[el.as_dict() for el in admin_panel_instance],
                                             ex=10)
    return {'books_request': books_request, 'page': page}
