Summary:	Touch typing tutor program
Summary(pl.UTF-8):	Program do nauki pisania bezwzrokowego na klawiaturze
Name:		klavaro
Version:	1.4.0
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/klavaro/%{name}-%{version}.tar.bz2
# Source0-md5:	a568aecd05f8eeb8a40c95fcf6de43d0
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://klavaro.sourceforge.net/en/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.6.2
BuildRequires:	gtkdatabox-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Klavaro is a program that teachs you to touch type and/or helps you to
improve your skills with the keyboard.

%description -l pl.UTF-8
Klavaro jest programem do nauki i/lub poprawy umiejętności pisania
bezwzrokowego na klawiaturze.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT


%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor


%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_iconsdir}/hicolor/*/*/*
