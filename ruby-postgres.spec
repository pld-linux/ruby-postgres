%define tarname ruby-postgres
Summary:	PostgreSQL module for Ruby
Summary(pl):	Modu³ PostgreSQL dla Ruby
Name:		ruby-Postgres
Version:	0.7.2
%define pre 20050412
Release:	0.%{pre}.2
License:	Ruby License
Group:		Development/Languages
Source0:	http://ruby.scripting.ca/postgres/archive/ruby-postgres-%{pre}.tar.gz
# Source0-md5:	34693e6468f8c20f1f0c039f7e101cdf
URL:		http://ruby.scripting.ca/postgres/
BuildRequires:	postgresql-devel
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby-modules
BuildRequires:	ruby-devel
Requires:	ruby-modules
Obsoletes:	ruby-postgres
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostgreSQL module for Ruby.

%description -l pl
Modu³ PostgreSQL dla Ruby.

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
