Name:           cdo
Version:        1.9.8
Release:        1
Summary:        Climate Data Operators
License:        GPLv2
URL:            https://code.zmaw.de/projects/cdo
Source:         https://code.mpimet.mpg.de/attachments/download/18264/cdo-%{version}.tar.gz
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  netcdf-cxx-devel
Requires:       netcdf

%description
CDO is a collection of command line Operators to manipulate and analyse Climate model Data.
Supported data formats are GRIB, netCDF, SERVICE, EXTRA and IEG. There are more than 400
operators available. The following table provides a brief overview of the main categories.


Authors:
--------
    This program was developed at the Max-Planck-Institute for Meteorology.
    Uwe Schulzweida, <uwe.schulzweida AT mpimet.mpg.de>, is the main author.
    Ralf Mueller, <ralf.mueller AT mpimet.mpg.de>
    Luis Kornblueh, <luis.kornblueh AT mpimet.mpg.de>
    Cedrick Ansorge, <cedrick.ansorge AT mpimet.mpg.de>
    Ralf Quast, <ralf.quast AT brockmann-consult.de>
    Send questions, comments and bug reports to <https://code.zmaw.de/projects/cdo>


%prep
%setup


%build
%configure --prefix=%{_prefix} --with-netcdf
make 

%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS OPERATORS README doc/cdo.pdf doc/cdo_refcard.pdf
%{_prefix}/bin/cdo

%changelog
* Fri Apr 24 2020 - Daniele Branchini <dbranchini@arpae.it> - 1.9.8-1
- Upstream update (fixes #1)

* Fri Sep 14 2018 - Daniele Branchini <dbranchini@arpae.it> - 1.9.5-1
- First build
