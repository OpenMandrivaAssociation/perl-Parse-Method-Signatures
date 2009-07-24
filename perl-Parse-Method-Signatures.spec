%define upstream_name   Parse-Method-Signatures
%define upstream_version  1.003009

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:    Turn parse TC data into Moose TC object
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRequires: perl(Data::Dump)
BuildRequires: perl(PPI)
BuildRequires: perl(aliased)
BuildRequires: perl(namespace::clean)
Requires: perl(MooseX::Traits)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Inspired by the Perl6::Signature manpage but streamlined to just support
the subset deemed useful for the TryCatch manpage and the
MooseX::Method::Signatures manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

