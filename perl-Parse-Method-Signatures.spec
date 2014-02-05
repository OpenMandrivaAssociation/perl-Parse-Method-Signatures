%define upstream_name   Parse-Method-Signatures
%define upstream_version 1.003016
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Epoch:		1

Summary:	Turn parse TC data into Moose TC object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/Parse-Method-Signatures-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Traits)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(MooseX::Types::Structured)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Balanced)
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(PPI)
BuildRequires:	perl(aliased)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

Requires:	perl(MooseX::Traits)

%description
Inspired by the Perl6::Signature manpage but streamlined to just support
the subset deemed useful for the TryCatch manpage and the
MooseX::Method::Signatures manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Parse


%changelog
* Sat Jan 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.3.13-1mdv2010.1
+ Revision: 487934
- update to 1.003013
- update to 1.003012

* Tue Sep 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.3.12-1mdv2010.0
+ Revision: 442945
- update to 1.003012

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.3.11-1mdv2010.0
+ Revision: 418419
- update to 1.003011

* Thu Aug 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.3.10-1mdv2010.0
+ Revision: 410677
- update to 1.003010

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.3.9-1mdv2010.0
+ Revision: 399262
- bumping epoch to take new version into account
- update to 1.003009
- using %%perl_convert_version
- fixed license field

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.003008-1mdv2010.0
+ Revision: 389801
- update to new version 1.003008

* Mon May 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.003007-1mdv2010.0
+ Revision: 379525
- update to new version 1.003007

* Sun May 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.003005-1mdv2010.0
+ Revision: 373929
- update to new version 1.003005

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.003004-1mdv2010.0
+ Revision: 370139
- update to new version 1.003004

* Wed Mar 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.003003-1mdv2009.1
+ Revision: 357183
- update to new version 1.003003

* Fri Mar 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.003002-1mdv2009.1
+ Revision: 349680
- update to new version 1.003002

* Wed Mar 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.003000-1mdv2009.1
+ Revision: 348641
- update to new version 1.003000

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.002000-2mdv2009.1
+ Revision: 343994
- fix dependencies

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.002000-1mdv2009.1
+ Revision: 343981
- import perl-Parse-Method-Signatures


* Sun Feb 22 2009 cpan2dist 1.002000-1mdv
- initial mdv release, generated with cpan2dist


