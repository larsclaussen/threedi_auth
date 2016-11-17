# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	user,
	organisation,
	roles,
	permissions,
)


class userCreateView(CreateView):

    model = user


class userDeleteView(DeleteView):

    model = user


class userDetailView(DetailView):

    model = user


class userUpdateView(UpdateView):

    model = user


class userListView(ListView):

    model = user


class organisationCreateView(CreateView):

    model = organisation


class organisationDeleteView(DeleteView):

    model = organisation


class organisationDetailView(DetailView):

    model = organisation


class organisationUpdateView(UpdateView):

    model = organisation


class organisationListView(ListView):

    model = organisation


class rolesCreateView(CreateView):

    model = roles


class rolesDeleteView(DeleteView):

    model = roles


class rolesDetailView(DetailView):

    model = roles


class rolesUpdateView(UpdateView):

    model = roles


class rolesListView(ListView):

    model = roles


class permissionsCreateView(CreateView):

    model = permissions


class permissionsDeleteView(DeleteView):

    model = permissions


class permissionsDetailView(DetailView):

    model = permissions


class permissionsUpdateView(UpdateView):

    model = permissions


class permissionsListView(ListView):

    model = permissions

