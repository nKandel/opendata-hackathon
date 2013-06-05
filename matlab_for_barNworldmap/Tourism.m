function varargout = Tourism(varargin)
% TOURISM MATLAB code for Tourism.fig
%      TOURISM, by itself, creates a new TOURISM or raises the existing
%      singleton*.
%
%      H = TOURISM returns the handle to a new TOURISM or the handle to
%      the existing singleton*.
%
%      TOURISM('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in TOURISM.M with the given input arguments.
%
%      TOURISM('Property','Value',...) creates a new TOURISM or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Tourism_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Tourism_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Tourism

% Last Modified by GUIDE v2.5 05-Jun-2013 11:37:20

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Tourism_OpeningFcn, ...
                   'gui_OutputFcn',  @Tourism_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Tourism is made visible.
function Tourism_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Tourism (see VARARGIN)

% Choose default command line output for Tourism
global percentYearwise;     %variable that stores the percentage of 16 countries from 2001 to 2011
global CountryName;
% global CountryHandle;
%global Index;
CountryName = {'Australia','Austria','Canada','China',...
                'Denmark','France','Germany','India',...
                'Italy','Japan','Netherlands','Spain',...
                'Switzerland','Sri lanka','U.S.A','U.K.'};
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Tourism wait for user response (see UIRESUME)
% uiwait(handles.figure1);
axes(handles.axes1);
axis off;
% worldmap('world');
% geoshow('landareas.shp');
% ylabel('Percentage');
% xlabel('Countries');
% 
% set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);

%rotateXLabels( gca(), 45 );
numericData=xlsread('Table\ourTable.xlsx');
percentYearwise = numericData(2:end,:);
percentYearwise= percentYearwise(2:2:end,:);
percentYearwise= percentYearwise(1:end-3,:);

% now normalize the result
% m = max(percentYearwise);
% for i=1:size(percentYearwise,2)
% percentYearwise(:,i) = percentYearwise(:,i)./m(i);
% end
% percentYearwise = floor(percentYearwise .* 100) ./ 100;
% [x Index] = sort(percentYearwise);

%size(percentYearwise)
% CountryHandle{1} = geoshow('Countries\Australia.shp');
% CountryHandle{2} = geoshow('Countries\Austria.shp');
% CountryHandle{3} = geoshow('Countries\Canada.shp');
% CountryHandle{4} = geoshow('Countries\China.shp');

% --- Outputs from this function are returned to the command line.
function varargout = Tourism_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on selection change in popupmenu1.
function popupmenu1_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1
global percentYearwise;     %variable that stores the percentage of 16 countries from 2001 to 2011
global CountryName;
% global CountryHandle;

option = get(handles.popupmenu1,'value');
y = percentYearwise(:,option-1);
switch option
    case 1
        set(handles.text1,'string','Please select year');
        return;
    case 2
        set(handles.text1,'string','2001');
        axes(handles.axes1);
        % make the bar plot
        bar(y,'linestyle','none');
        ylabel('Percentage');
        xlabel('Countries');

        set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);
        rotateXLabels( gca(), 45 );
 %       set(get(CountryHandle{1},'Children'),'FaceColor',[1 0 0],'FaceAlpha',0.25);
 %       set(get(CountryHandle{1},'Children'),'FaceColor',[1 0 0],'FaceAlpha',0.25);
 %       set(get(CountryHandle{1},'Children'),'FaceColor',[1 0 0],'FaceAlpha',0.25);
%        set(get(CountryHandle{2},'Children'),'FaceColor',[1 0 0],'FaceAlpha',countryAlpha(2));
%         for i=1:4
%             set(get(CountryHandle{i},'Children'),'FaceColor',[1 0 0],'FaceAlpha',countryAlpha(i));
%         end
    case 3
        set(handles.text1,'string','2002');
        axes(handles.axes1);
        % make the bar plot
        bar(y,'linestyle','none');
        ylabel('Percentage');
        xlabel('Countries');

        set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);
        rotateXLabels( gca(), 45 );
    case 4
        set(handles.text1,'string','2003');
        axes(handles.axes1);
        % make the bar plot
        bar(y,'linestyle','none');
        ylabel('Percentage');
        xlabel('Countries');

        set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);
        rotateXLabels( gca(), 45 );
    case 5
        set(handles.text1,'string','2004');
        axes(handles.axes1);
        % make the bar plot
        bar(y,'linestyle','none');
        ylabel('Percentage');
        xlabel('Countries');

        set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);
        rotateXLabels( gca(), 45 );
    case 6
        set(handles.text1,'string','2005');
        axes(handles.axes1);
        % make the bar plot
        bar(y,'linestyle','none');
        ylabel('Percentage');
        xlabel('Countries');

        set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);
        rotateXLabels( gca(), 45 );
    case 7
        set(handles.text1,'string','2006');
        axes(handles.axes1);
        % make the bar plot
        bar(y,'linestyle','none');
        ylabel('Percentage');
        xlabel('Countries');

        set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);
        rotateXLabels( gca(), 45 );
    case 8
        set(handles.text1,'string','2007');
        set(handles.text1,'string','2006');
        axes(handles.axes1);
        % make the bar plot
        bar(y,'linestyle','none');
        ylabel('Percentage');
        xlabel('Countries');

        set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);
        rotateXLabels( gca(), 45 );
    case 9
        set(handles.text1,'string','2008');
        set(handles.text1,'string','2006');
        axes(handles.axes1);
        % make the bar plot
        bar(y,'linestyle','none');
        ylabel('Percentage');
        xlabel('Countries');

        set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);
        rotateXLabels( gca(), 45 );
    case 10
        set(handles.text1,'string','2009');
        set(handles.text1,'string','2006');
        axes(handles.axes1);
        % make the bar plot
        bar(y,'linestyle','none');
        ylabel('Percentage');
        xlabel('Countries');

        set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);
        rotateXLabels( gca(), 45 );
    case 11
        set(handles.text1,'string','2010');
        set(handles.text1,'string','2006');
        axes(handles.axes1);
        % make the bar plot
        bar(y,'linestyle','none');
        ylabel('Percentage');
        xlabel('Countries');

        set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);
        rotateXLabels( gca(), 45 );
    case 12
        set(handles.text1,'string','2011');
        set(handles.text1,'string','2006');
        axes(handles.axes1);
        % make the bar plot
        bar(y,'linestyle','none');
        ylabel('Percentage');
        xlabel('Countries');

        set(gca,'Fontsize',11,'XTick',1:16,'XTickLabel',CountryName);
        rotateXLabels( gca(), 45 );
    
end


% --- Executes during object creation, after setting all properties.
function popupmenu1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
