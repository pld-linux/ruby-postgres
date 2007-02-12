%define tarname ruby-postgres
Summary:	PostgreSQL module for Ruby
Summary(pl.UTF-8):   Moduł PostgreSQL dla Ruby
Name:		ruby-Postgres
Version:	0.7.2
%define pre 20050412
Release:	0.%{pre}.4
License:	Ruby License
Group:		Development/Languages
Source0:	http://ruby.scripting.ca/postgres/archive/ruby-postgres-%{pre}.tar.gz
# Source0-md5:	34693e6468f8c20f1f0c039f7e101cdf
URL:		http://ruby.scripting.ca/postgres/
BuildRequires:	postgresql-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8.4-5
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-postgres
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostgreSQL module for Ruby.

%description -l pl.UTF-8
Moduł PostgreSQL dla Ruby.

%prep
%setup -q -n %{tarname}

%build
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{ruby_archdir}/postgres.so
