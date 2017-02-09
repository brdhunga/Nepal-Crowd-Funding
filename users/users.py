

class UserDataMixin:

    def deny_access(self):
        """Replaces the default PermissionDenied()"""
        messages.error(
            self.request,
            'Sorry! You do not have permission to access the page.'
        )
        return redirect('home')


    def deny_access_via_404(self, message):
        """Raise a 404 Not Found with custom message."""
        raise Http404(message)

    