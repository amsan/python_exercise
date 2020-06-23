def pagination(current_page, total_pages, boundaries, around):
    pages = range(1, total_pages + 1)
    page_range = list(filter(lambda page: (page <= boundaries and page < current_page) or page >= (total_pages - boundaries + 1) or page >= (current_page - around) and page <= (current_page + around), pages))
    page_range_with_dots = []
    append = page_range_with_dots.append
    verify_page = None

    for page in page_range:
        if verify_page is not None and page - verify_page != 1:
            append('...')
                
        append(page)
        verify_page = page

    print(page_range_with_dots)
    return page_range_with_dots
