Name:		python-vobject
Version:	0.9.9
Release:	2
Summary:	A full-featured Python package for parsing and creating iCalendar and
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/vobject/
Source0:	vobject-0.9.9.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(python-dateutil)
BuildRequires:	python%{pyver}dist(pytz)
BuildArch:	noarch
%description
A full-featured Python package for parsing and creating iCalendar and.

%files
%{py_sitedir}/*
%{_bindir}/*
