def pagination(current_page, total_pages, boundaries, around):
    page_range = []
    page_range_with_dots = []
    l = None

    for page in range(1, total_pages + 1):
        if (page <= boundaries and page < current_page) or page >= (total_pages - boundaries + 1) or page >= (current_page - around) and page <= (current_page + around):
            page_range.append(page)
    
    for page in page_range:
        if l is not None:
            if page - l != 1:
                page_range_with_dots.append('...')
                
        page_range_with_dots.append(page)
        l = page

    print(page_range_with_dots)
    return page_range_with_dots

pagination(4, 5, 1, 0)