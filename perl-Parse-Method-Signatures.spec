%define module   Parse-Method-Signatures
%define version  1.003000
%define release  %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Turn parse TC data into Moose TC object
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Parse/%{module}-%{version}.tar.gz
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Traits)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(MooseX::Types::Moose)
BuildRequires: perl(MooseX::Types::Structured)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Balanced)
BuildRequires: perl(aliased)
BuildRequires: perl(namespace::clean)
Requires: perl(MooseX::Traits)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Inspired by the Perl6::Signature manpage but streamlined to just support
the subset deemed useful for the TryCatch manpage and the
MooseX::Method::Signatures manpage.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/Parse

