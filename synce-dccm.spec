Summary:	SynCE DCCM - daemon to communicate with Pocket PC device
Summary(pl):	SynCE DCCM - demon do komunikacji z urz±dzeniem Pocket PC
Name:		synce-dccm
Version:	0.9.0
Release:	1
License:	MIT
Group:		Libraries
Source0: 	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	a32607bf423e5e5467b80edc2b7dac5d
URL:		http://synce.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRequires:	synce-libsynce-devel >= 0.9.0
# for play
Requires:	sox
Requires:	synce-libsynce >= 0.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DCCM is a daemon required to be able to communicate with a handheld
device. It's part of SynCE project.

%description -l pl
DCCM to demon potrzebny do komunikowania siê z urz±dzeniem Pocket PC.
Jest on czê¶ci± projektu SynCE.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
