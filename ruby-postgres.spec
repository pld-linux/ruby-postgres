%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
Summary:	PostgreSQL module for Ruby
Summary(pl):	Modu³ PostgreSQL dla Ruby
Name:		ruby-Postgres
Version:	0.7.1
Release:	1
License:	Ruby License
Group:		Development/Languages
Source0:	http://www.postgresql.jp/interfaces/ruby/archive/%{name}-%{version}.tar.gz
# Source0-md5:	8ef67b3f4b089248f0420baeb0e3b3c8
URL:	http://www.postgresql.jp/interfaces/ruby/
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	postgresql-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostgreSQL module for Ruby.

%description -l pl
Modu³ PostgreSQL dla Ruby.

%prep
%setup -q

%build
ruby extconf.rb
%{__make}

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
%{ruby_archdir}/*
