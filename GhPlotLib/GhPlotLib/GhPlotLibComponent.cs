using System;
using System.Collections.Generic;

using Grasshopper.Kernel;
using Rhino.Geometry;
using System.IO;
using System.Diagnostics;

namespace GhPlotLib
{
    public class GhPlotLibComponent : GH_Component
    {
        string subFolder = DateTime.Now.ToString("yyyyMMdd_Hmm") + @"\";
        string workingDir = @"C:\GhPlotLib\TEMP\";

        bool processExited = false;
        Process process2 = new Process();
        /// <summary>
        /// Each implementation of GH_Component must provide a public 
        /// constructor without any arguments.
        /// Category represents the Tab in which the component will appear, 
        /// Subcategory the panel. If you use non-existing tab or panel names, 
        /// new tabs/panels will automatically be created.
        /// </summary>
        public GhPlotLibComponent()
            : base("GhPlotLib", "GhP",
                "Scientific plotting for grasshopper",
                "GhPlotLib", "00_GHPlotLib")
        {
            workingDir += subFolder;
            if (!Directory.Exists(workingDir))
                Directory.CreateDirectory(workingDir);

            process2.StartInfo.FileName = "doAllWork.py";
            process2.EnableRaisingEvents = true;
            process2.StartInfo.CreateNoWindow = true;
            process2.StartInfo.UseShellExecute = true;
            process2.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            process2.Exited += process_Exited;
        }

        private void process_Exited(object sender, EventArgs e)
        {
            processExited = true;
        }

        /// <summary>
        /// Registers all the input parameters for this component.
        /// </summary>
        protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager)
        {
            pManager.AddBooleanParameter("initiate GHPLOTLIB    |\n", "", "", GH_ParamAccess.item);
            pManager.AddTextParameter("workingDir    |", "", "", GH_ParamAccess.item, workingDir);
        }

        /// <summary>
        /// Registers all the output parameters for this component.
        /// </summary>
        protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager)
        {
            pManager.AddTextParameter("|    Log ... \n", "", "", GH_ParamAccess.item);
        }

        /// <summary>
        /// This is the method that actually does the work.
        /// </summary>
        /// <param name="DA">The DA object can be used to retrieve data from input parameters and 
        /// to store data in output parameters.</param>
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            bool initiate = false;

            string datalog = ""; 
            string[,] data;
            if (!DA.GetData(0, ref initiate)) { return; }
            if (!initiate) { return; }
            if (!DA.GetData(1, ref workingDir)) { return; }
            process2.StartInfo.WorkingDirectory = workingDir;

            data = new string[1,2] { { "##workingDir##", workingDir.Replace("\\", "\\\\") } };

            try
            {
                writefile(data, Resources.texts._initNumpyMatplotLib, workingDir);
                process2.Start();
                while(!processExited)
                {

                }
                datalog += File.ReadAllText(workingDir + "logfile.txt");
            }catch (Exception e)
            {
                datalog += "\n" + e.ToString() + "\n";
            }

            DA.SetData(0, datalog);
            process2.Close();
            

        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="data"></param>
        /// <param name="PythonFile"></param>
        /// <param name="workingDir_"></param>
        private void writefile(string[,] dataArray, string PythonFile, string workingDir_)
        {
            string textfile = "";
            if (dataArray.Length > 1)
            {
                for (int i = 0; i < dataArray.Length-1; i++)
                {
                    textfile = PythonFile.Replace(dataArray[i, 0], dataArray[i, 1]);
                    File.AppendAllText(workingDir_ + "doAllWork.py", textfile);
                }
            }
            else
            {
                textfile = PythonFile.Replace(dataArray[0, 0], dataArray[0, 1]);
            }
            File.AppendAllText(workingDir_ + "doAllWork.py", textfile);

        }



        /// <summary>
        /// Provides an Icon for every component that will be visible in the User Interface.
        /// Icons need to be 24x24 pixels.
        /// </summary>
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                // You can add image files to your project resources and access them like this:

                return Resources.Icons.GHplot5;
            }
        }
        /// <summary>
        /// Each component must have a unique Guid to identify it. 
        /// It is vital this Guid doesn't change otherwise old ghx files 
        /// that use the old ID will partially fail during loading.
        /// </summary>
        public override Guid ComponentGuid
        {
            get { return new Guid("{979be763-af5c-4095-913a-2f6c23de2fa0}"); }
        }
    }
}
