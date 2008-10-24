Summary:	Simple yet powerful mind-mapping tool for the GNOME
Summary(pl.UTF-8):	Proste lecz potężne narzędzie do mapek umysłu dla GNOME
Name:		labyrinth
Version:	0.4.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/labyrinth/0.4/%{name}-%{version}.tar.gz
# Source0-md5:	465139aeeb039779295dd7f46dc1a48d
URL:		http://www.gnome.org/~dscorgie/
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-desktop-devel >= 2.14
BuildRequires:	intltool >= 0.35.0
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-gnome-devel >= 2.12
BuildRequires:	python-pycairo-devel >= 1.0
BuildRequires:	python-pygobject-devel >= 2.10
BuildRequires:	python-pygtk-devel >= 2:2.8
BuildRequires:	rpm-pythonprov
Requires:	python-Numeric
Requires:	python-PyXML
Requires:	python-pygobject >= 2.10
Requires:	python-pygtk-glade >= 2:2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Labyrinth is a lightweight mind-mapping tool, written in Python using
GTK+ and Cairo to do the drawing. It is intended to be as light and
intuitive as possible, but still provide a wide range of powerful
features.

A mind-map is a diagram used to represent words, ideas, tasks or other
items linked to and arranged radially around a central key word or
idea. It is used to generate, visualize, structure and classify ideas,
and as an aid in study, organization, problem solving, and decision
making.

%description -l pl.UTF-8
Labyrinth to lekkie narzędzie do mapek umysłu, napisane w Pythonie z
użyciem GTK+ i Cairo do rysowania. W zamierzeniu ma być najlżejsze
i najbardziej intuicyjne jak to możliwe jednocześnie dostarczając
szeroki zakres potężnych możliwości.

Mapa umysłu to diagram używany do reprezentacji słów, idei, zadań
albo innych elementów połączonych i ułożonych koliście wokół
centralnego słowa-klucza lub idei. Jest wykorzystywana do
generowania, wizualizowania, strukturalizowania i klasyfikowania
pomysłów i jako pomoc w nauce, organizacji, rozwiązywaniu
problemów i podejmowaniu decyzji.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/labyrinth
%{_iconsdir}/hicolor/*/apps/labyrinth.*
%{_desktopdir}/labyrinth.desktop
%dir %{py_sitescriptdir}/labyrinth
%{py_sitescriptdir}/labyrinth/*.py[co]
