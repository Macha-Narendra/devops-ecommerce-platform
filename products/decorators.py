from django.contrib.auth.decorators import user_passes_test


def admin_required(view_func):

    decorated_view = user_passes_test(
        lambda u: u.is_staff
    )(view_func)

    return decorated_view
