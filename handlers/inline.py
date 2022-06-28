from aiogram import types, Dispatcher
import hashlib
from youtube_search import YoutubeSearch as YT


def finder(text):
    results = YT(text, max_results=10).to_dict()
    return results


async def inline_youtube_handler(query: types.InlineQuery):
    text = query.query or "echo"
    links = finder(text)
    articles = [
        types.InlineQueryResultArticle(
            id=hashlib.md5(f"{link['id']}".encode()).hexdigest(),
            title=link["title"],
            url=f"https://www.youtube.com/watch?v={link['id']}",
            thumb_url=f"{link['thumbnails'][0]}",
            input_message_content=types.InputMessageContent(
                message_text=f"https://www.youtube.com/watch?v={link['id']}"
            )
        ) for link in links
    ]
    await query.answer(articles, cache_time=60, is_personal=True)


async def inline_wiki_handler(query: types.InlineQuery):
    text = query.query or "echo"
    links = f"https://ru.wikipedia.org/wiki/{text}"
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    articles = [
        types.InlineQueryResultArticle(
            id=result_id,
            title="Wiki: ",
            url=links,
            input_message_content=types.InputMessageContent(
                message_text=links
            )
        )
    ]
    await query.answer(articles, cache_time=2, is_personal=True)

def register_handler_inline(dp: Dispatcher):
    # dp.register_inline_handler(inline_youtube_handler)
    dp.register_inline_handler(inline_wiki_handler)
