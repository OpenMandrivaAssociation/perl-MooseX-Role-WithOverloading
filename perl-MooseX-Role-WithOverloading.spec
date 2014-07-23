%define upstream_name MooseX-Role-WithOverloading
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Roles which support overloading
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz
Source1:	%{name}.rpmlintrc

BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(XSLoader)
BuildRequires:	perl(aliased)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl-devel

Requires:	perl(aliased)
Requires:	perl(namespace::autoclean)
Requires:	perl(namespace::clean)

%description
MooseX::Role::WithOverloading allows you to write a the Moose::Role manpage
which defines overloaded operators and allows those operator overloadings
to be composed into the classes/roles/instances it's compiled to, while
plain the Moose::Role manpages would lose the overloading.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod go+r -R .

%build
perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*
