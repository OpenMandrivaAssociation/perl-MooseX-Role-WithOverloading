%define upstream_name MooseX-Role-WithOverloading
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

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


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.90.0-2
+ Revision: 773618
- fix non-readable
- clean out spec
- add filter exception on description-line-too-long for debug package
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jan 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 628581
- update to new version 0.09

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 561038
- update to 0.08

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 556009
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 552421
- update to 0.06

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.1
+ Revision: 488604
- update to 0.05

* Tue Jan 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 486307
- update to 0.04

* Mon Nov 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-2mdv2010.1
+ Revision: 469244
- bump mkrel
- adding missing requires:

* Sun Nov 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.1
+ Revision: 468963
- import perl-MooseX-Role-WithOverloading


* Sun Nov 22 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist
