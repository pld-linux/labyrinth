Summary:	Simple yet powerful mind-mapping tool for the GNOME
Summary(pl.UTF-8):Proste lecz potężne narzędzie do mapek umysłu dla GNOME
Name:		labyrinth
Version:	0.3
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/labyrinth/0.3/%{name}-%{version}.tar.gz
# Source0-md5:	f7122423d8780053ec8de8c77cc7295b
URL:		http://www.gnome.org/~dscorgie/
BuildRequires:	gcc
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	python-gnome-devel >= 2.0
BuildRequires:	python-pycairo-devel
BuildRequires:	python-pygobject-devel
BuildRequires:	python-pygtk-devel
Requires:	python-PyXML
Requires:	python-pygtk-glade
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Labyrinth is a lightweight mind-mapping tool, written in Python using
Gtk and Cairo to do the drawing. It is intended to be as light and
intuitive as possible, but still provide a wide range of powerful
features.

A mind-map is a diagram used to represent words, ideas, tasks or other
items linked to and arranged radially around a central key word or
idea. It is used to generate, visualize, structure and classify ideas,
and as an aid in study, organization, problem solving, and decision
making.

%description -l pl.UTF-8
Labyrinth to lekkie narzędzie do mapek umysłu, napisane w Pythonie
używająć Gtk i Cairo do rysowania. W zamiarach ma być najlżejsze
i najbardziej intuicyjne jak to możliwe jednocześnie dostarczając
szeroki zakres potężnych cech.

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/labyrinth/
%{_iconsdir}/hicolor/*/apps/labyrinth.*
%{_desktopdir}/labyrinth.desktop
%dir %{py_sitescriptdir}/labyrinth
%{py_sitescriptdir}/labyrinth/*.pyc
